# Expanding Scope of Genetic Studies in the Era of Biobanks

- 저자: Dutta D (NCI), Chatterjee N (Johns Hopkins Univ.)
- 출처: *Human Molecular Genetics* (Author manuscript, PMC 2026)
- 유형: 리뷰

## 요약

바이오뱅크가 GWAS의 규모와 범위를 확장한 과정을 정리한 리뷰임. 바이오뱅크 설계 유형, 질환 컨소시엄과의 통합, PRS, 다면발현, post-GWAS, 멀티오믹스, 시퀀싱 연구로 나누어 다룸. 표본 선택 편향과 표현형 오분류를 주요 한계로 지적함.

## 1. 바이오뱅크 유형

| 유형 | 대표 사례 | 장점 | 한계 |
|---|---|---|---|
| 인구집단 기반 | UK Biobank, FinnGen, Estonian Biobank, Biobank Japan, China Kadoorie, H3Africa, Mexican Biobank | 대규모 표본, 종단 추적, 등록부 기반의 완전한 질환 파악 | 건강한 자원자 편향, 특정 질환 표현형의 깊이 부족 |
| EHR·병원 기반 | BioVU, MGI, BioMe, Mass General Brigham, All of Us, Million Veteran Program | 진단·처방·검사 등 실제 임상 데이터 연계, 약물유전체 연구 | 의료체계 이탈로 인한 비무작위 결측, 코딩 오류로 인한 오분류 |
| 출생 코호트 | ALSPAC, MoBa, Generation R | 생애 초기 노출과 장기 건강 결과 연구 | 추적 비용이 크고 성인 발병 질환에는 제한적 |
| 임상시험 | NCI-MATCH, Biomarkers Consortium | 표준화된 고품질 표현형, 약물 반응 연구 | 규모가 작음 |

## 2. 질환 컨소시엄과 바이오뱅크 통합

- 바이오뱅크는 유병률이 낮은 질환의 사례 수가 부족함. 질환 컨소시엄은 환경·위험요인 정보가 부족함.
- 요약통계 기반 메타분석이 표준임. 개인정보와 접근 제약을 피할 수 있음.
- 한계: 공통으로 조화된 모수만 결합할 수 있음.
- 대안: 제약 최대우도 기반 데이터 통합(Chatterjee 2016), 일반화 메타분석(Kundu 2019).

## 3. 대규모 GWAS 방법

| 도구 | 기능 |
|---|---|
| SAIGE | 사례·대조군 불균형과 표본 근연관계를 보정하는 대규모 GWAS |
| REGENIE | 전장 유전체 회귀 기반의 효율적 연속형·이진형 형질 GWAS |
| LDSC (LD Score Regression) | 유전율 추정, 교란과 다유전성 구분 |
| Stratified LDSC | 기능 주석별 유전율 분할 |
| GENESIS 계열 (Zhang 2018) | 요약통계 기반 효과크기 분포 및 다유전성 추정 |

※ SAIGE·REGENIE·GENESIS는 본문에 이름이 없고 인용 문헌(57, 58, 52)에 근거해 표기함.

## 4. 다인종 분석

| 도구 | 기능 |
|---|---|
| MR-MEGA | 조상(ancestry)을 반영한 다인종 메타회귀 |
| Tractor | 국소 조상(local ancestry)을 반영해 혼혈 개인을 GWAS에 포함 |
| CT-SLEB | 다인종 PRS |
| MUSSEL | 베이지안 다인종 PRS |
| PROSPER | 앙상블 penalized 회귀 기반 다인종 PRS |
| SuSiEx | 다인종 fine-mapping |
| MultiSuSiE | All of Us WGS 기반 다인종 fine-mapping |

- 유전적 조상을 이산 범주가 아닌 연속체로 다루는 방향이 확산되고 있음.

## 5. PRS 개발 및 보정

- 대규모 표본 덕분에 효과가 작은 변이도 검출하여 예측력이 향상됨.
- 핵심 활용은 보정(calibration)임. 종단 발생률 데이터(UKB, FinnGen, Estonian)로 예측 위험과 실제 발생률을 비교함.
- 다형질 PRS: mtPGS, Multi-PGS. 다면발현을 이용해 정확도를 높임.

## 6. 다면발현 (Pleiotropy)

| 도구 | 기능 |
|---|---|
| LDSC (cross-trait) | 형질 간 유전상관 추정 |
| Genomic SEM | 다변량 유전 구조 모델링 |
| PheWAS | 변이 하나를 다수 표현형과 연관 분석 (BioVU, UKB, FinnGen, AoU) |

## 7. Post-GWAS 분석

| 분석 | 도구·자원 | 바이오뱅크의 기여 |
|---|---|---|
| Fine-mapping | SuSiEx, MultiSuSiE | 대규모 LD 참조, 다인종 LD 차이로 해상도 향상 |
| 멘델 무작위화(MR) | MR-Base, 다변수 MR | 표현형이 풍부해 노출 변수를 다양하게 설정 가능, 종단 데이터로 시점별 노출 효과 구분 |

## 8. 멀티오믹스

| 구분 | 도구·자원 | 내용 |
|---|---|---|
| 외부 참조 | GTEx, eQTLGen, ENCODE | eQTL 및 조절 요소 참조 |
| 통합 방법 | PrediXcan, TWAS, PWAS, trans-eQTL 분석 | 유전자·단백질 수준 연관 분석 |
| 단백체 | SomaScan, Olink | UKB-PPP에서 54,219명의 혈장 단백질 측정. pQTL과 MR로 질환 기전과 약물 표적 발굴 |
| 대사체 | NMR 대사체 패널 | 대사 질환 연구 |
| 영상 | 뇌 MRI, X-ray (UKB) | 영상 표현형 GWAS |

- 전사체·후성유전체·메타유전체는 비용 문제로 아직 제한적임.

## 9. 시퀀싱 연구 (희귀 변이)

| 방식 | 장점 | 한계 |
|---|---|---|
| WES | 비용 효율적, 효과가 큰 희귀 암호화 변이 검출. 현재 실질적 발견의 대부분을 차지함 | 비암호화·조절 변이 누락 |
| WGS | 비암호화 변이, 구조변이, 조절 요소 검출 | 비용과 저장 부담이 크고 해석이 어려움. 발견 성과는 아직 제한적임 |

- 다인종 시퀀싱(AoU)은 조상 특이 희귀 변이를 발굴하는 데 유리하지만, 집단 층화 보정이 필요함.

## 10. 과제 및 전망

- 선택 편향: 자원자 중심으로 저소득층과 중증 환자가 과소대표됨(UKB).
- 표현형 오분류: EHR 코딩 관행의 차이에서 발생함.
- 윤리: 개인정보 보호, 동의, 데이터 접근 거버넌스가 필요함.
- 정밀의료: PRS 기반 고위험군 선별 검진, 멀티오믹스 위험 예측, 유전체 결과 환원(eMERGE, Our Future Health).
