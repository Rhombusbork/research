"""정량약리학 1시간 수업용 시뮬레이터.

쉼표로 여러 값을 주면 곡선을 겹쳐 그린다. 예: --V 10,20
그림은 figs/ 에 저장된다.

  python sim.py single   --dose 100 --CL 5 --V 10,20
  python sim.py multi    --dose 100 --CL 5 --V 50 --tau 12 --n 10
  python sim.py emax     --Emax 100 --EC50 2 --hill 1 --C 5,10
  python sim.py indirect --kout 0.05,0.5
  python sim.py pop      --nsub 100 --nsamp 2
  python sim.py decide   --flat 200 --perkg 3
"""
import argparse, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings("ignore")

os.makedirs("figs", exist_ok=True)
L = lambda s: [float(x) for x in str(s).split(",")]


def save(name):
    path = f"figs/{name}.png"
    plt.tight_layout(); plt.savefig(path, dpi=120); plt.close()
    print(f"그림 저장: {path}")


def conc(t, dose, CL, V, tau=None, n=1):
    k = CL / V
    C = np.zeros_like(t)
    for i in range(n):
        t0 = 0 if tau is None else i * tau
        C += np.where(t >= t0, dose / V * np.exp(-k * (t - t0)), 0)
    return C


def single(a):
    t = np.linspace(0, a.tmax, 2000)
    for d in L(a.dose):
        for cl in L(a.CL):
            for v in L(a.V):
                C = conc(t, d, cl, v)
                auc = np.trapezoid(C, t)
                print(f"dose={d:g} CL={cl:g} V={v:g} | C0={d/v:.2f}  반감기={0.693*v/cl:.2f}h  AUC={auc:.1f}  (dose/CL={d/cl:.1f})")
                plt.plot(t, C, label=f"dose={d:g}, CL={cl:g}, V={v:g}")
    plt.xlabel("time (h)"); plt.ylabel("concentration"); plt.legend(); save("single")


def multi(a):
    tmax = a.tau * a.n
    t = np.linspace(0, tmax, 4000)
    for d in L(a.dose):
        for cl in L(a.CL):
            for v in L(a.V):
                C = conc(t, d, cl, v, a.tau, a.n)
                th = 0.693 * v / cl
                # 각 투여 직전의 최저농도(trough)로 정상상태 도달을 판단
                tr_t = np.array([i * a.tau for i in range(1, a.n)])
                tr = np.array([conc(np.array([x - 1e-9]), d, cl, v, a.tau, a.n)[0] for x in tr_t])
                tr_ss = d / v * np.exp(-cl / v * a.tau) / (1 - np.exp(-cl / v * a.tau))
                t90 = tr_t[np.argmax(tr >= 0.9 * tr_ss)] if (tr >= 0.9 * tr_ss).any() else float("nan")
                print(f"dose={d:g} CL={cl:g} V={v:g} | 반감기={th:.1f}h  정상상태 최저농도={tr_ss:.2f}  그 90% 도달≈{t90:.0f}h ({t90/th:.1f} 반감기)  평균 정상상태 농도={d/cl/a.tau:.2f}")
                plt.plot(t, C, label=f"dose={d:g}, CL={cl:g}, V={v:g}")
    plt.xlabel("time (h)"); plt.ylabel("concentration"); plt.legend(); save("multi")


def emax(a):
    C = np.logspace(-2, 3, 500)
    for E in L(a.Emax):
        for ec in L(a.EC50):
            for h in L(a.hill):
                f = lambda c: E * c**h / (ec**h + c**h)
                plt.semilogx(C, f(C), label=f"Emax={E:g}, EC50={ec:g}, hill={h:g}")
                for c in L(a.C):
                    print(f"EC50={ec:g} hill={h:g} | 농도 {c:g} → 효과 {f(c):.1f}  /  농도 {2*c:g} → 효과 {f(2*c):.1f}")
    plt.xlabel("concentration (log)"); plt.ylabel("effect"); plt.legend(); save("emax")


def indirect(a):
    # 모델 I: 약물이 매개체 생성(kin)을 억제. R0 = kin/kout = 100
    dt = 0.05; t = np.arange(0, a.tmax, dt)
    C = conc(t, a.dose, a.CL, a.V)
    fig, ax = plt.subplots(2, 1, sharex=True)
    ax[0].plot(t, C, "k"); ax[0].set_ylabel("drug concentration")
    for ko in L(a.kout):
        kin = 100 * ko; R = np.empty_like(t); R[0] = 100
        for i in range(1, len(t)):
            inh = 1 - C[i-1] / (a.IC50 + C[i-1])
            R[i] = R[i-1] + dt * (kin * inh - ko * R[i-1])
        print(f"kout={ko:g} | 농도 최고 시점 {t[np.argmax(C)]:.1f}h, 반응 최저 시점 {t[np.argmin(R)]:.1f}h, 최저 반응 {R.min():.1f}")
        ax[1].plot(t, R, label=f"kout={ko:g} (mediator t1/2 {0.693/ko:.1f}h)")
    ax[1].set_ylabel("response (mediator level)"); ax[1].set_xlabel("time (h)"); ax[1].legend(); save("indirect")


def pop(a):
    rng = np.random.default_rng(a.seed)
    V, CLpop, omega, sigma = 50.0, 5.0, a.omega, a.sigma
    reps = 200; m_est, w_est = [], []
    times = np.linspace(1, 24, a.nsamp)
    for _ in range(reps):
        CLi = CLpop * np.exp(rng.normal(0, omega, a.nsub))
        logk = []
        for cl in CLi:
            ts = rng.choice(times, size=a.nsamp, replace=False) if a.nsamp > 2 else times
            y = np.log(100 / V) - cl / V * ts + rng.normal(0, sigma, a.nsamp)
            logk.append(np.log(max(-np.polyfit(ts, y, 1)[0], 1e-4)))
        logk = np.array(logk)
        m_est.append(np.exp(logk.mean()) * V)
        # 측정 오차가 만든 퍼짐을 빼고 진짜 개인차만 추정

        w_est.append(np.sqrt(max(np.var(logk), 0)))
    m_est, w_est = np.array(m_est), np.array(w_est)
    print(f"설계: {a.nsub}명 × {a.nsamp}회 = 총 {a.nsub*a.nsamp}회 채혈 (참값: 전형적 CL={CLpop}, 개인차 ω={omega})")
    print(f"  전형적 CL 추정: 평균 {m_est.mean():.2f}, 반복 실험 간 흔들림 ±{m_est.std():.2f}")
    print(f"  개인차 ω 추정: 평균 {w_est.mean():.2f}, 반복 실험 간 흔들림 ±{w_est.std():.2f}")
    plt.hist(w_est, bins=30); plt.axvline(omega, color="k", ls="--", label="true value")
    plt.xlabel("estimated between-subject variability omega"); plt.legend(); plt.title(f"{a.nsub} subjects x {a.nsamp} samples"); save(f"pop_{a.nsub}x{a.nsamp}")


def decide(a):
    rng = np.random.default_rng(a.seed)
    WT = np.clip(rng.lognormal(np.log(70), 0.25, 5000), 35, 150)
    CL = 5 * (WT / 70) ** 0.75 * np.exp(rng.normal(0, 0.3, WT.size))
    lo, hi = L(a.target)
    for name, lab, dose in [(f"고정 {a.flat:g} mg", f"flat {a.flat:g} mg", np.full_like(WT, a.flat)), (f"체중당 {a.perkg:g} mg/kg", f"{a.perkg:g} mg/kg", a.perkg * WT)]:
        auc = dose / CL
        inside = np.mean((auc >= lo) & (auc <= hi)) * 100
        print(f"{name:>16} | AUC 중앙값 {np.median(auc):.0f}, 목표 범위 [{lo:g},{hi:g}] 안 {inside:.0f}%, 미달 {np.mean(auc<lo)*100:.0f}%, 초과 {np.mean(auc>hi)*100:.0f}%")
        plt.hist(auc, bins=60, alpha=0.5, label=lab)
    plt.axvspan(lo, hi, color="g", alpha=0.1, label="target window")
    plt.xlabel("exposure AUC"); plt.legend(); save("decide")


p = argparse.ArgumentParser()
s = p.add_subparsers(dest="mode", required=True)
for m in ["single", "multi"]:
    q = s.add_parser(m); q.add_argument("--dose", default="100"); q.add_argument("--CL", default="5"); q.add_argument("--V", default="50")
    q.add_argument("--tmax", type=float, default=200); q.add_argument("--tau", type=float, default=12); q.add_argument("--n", type=int, default=10)
q = s.add_parser("emax"); q.add_argument("--Emax", default="100"); q.add_argument("--EC50", default="2"); q.add_argument("--hill", default="1"); q.add_argument("--C", default="1")
q = s.add_parser("indirect"); q.add_argument("--kout", default="0.05,0.5"); q.add_argument("--dose", type=float, default=100)
q.add_argument("--CL", type=float, default=5); q.add_argument("--V", type=float, default=50); q.add_argument("--IC50", type=float, default=0.5); q.add_argument("--tmax", type=float, default=120)
q = s.add_parser("pop"); q.add_argument("--nsub", type=int, default=100); q.add_argument("--nsamp", type=int, default=2)
q.add_argument("--omega", type=float, default=0.3); q.add_argument("--sigma", type=float, default=0.1); q.add_argument("--seed", type=int, default=1)
q = s.add_parser("decide"); q.add_argument("--flat", type=float, default=200); q.add_argument("--perkg", type=float, default=3)
q.add_argument("--target", default="25,60"); q.add_argument("--seed", type=int, default=1)
a = p.parse_args()
{"single": single, "multi": multi, "emax": emax, "indirect": indirect, "pop": pop, "decide": decide}[a.mode](a)
