# Current Bioinformatics Tools in Precision Oncology

- 저자: Wolde T, Bhardwaj V, Pandey V (Tsinghua Univ.)
- 출처: *MedComm* 2025;6:e70243. https://doi.org/10.1002/mco2.70243
- 유형: 리뷰

## 요약

정밀종양학의 바이오마커 발굴에 쓰이는 생물정보학 도구를 오믹스 계층별, 분석 단계별로 정리한 리뷰임. 멀티오믹스 통합, AI/ML, 단일세포·공간 오믹스를 핵심 축으로 제시함. 데이터 이질성, 계산 자원, 임상 적용, 윤리 문제를 주요 과제로 지적함.

## 1. 전처리 및 품질관리

| 도구 | 기능 |
|---|---|
| FastQC | 원시 리드 품질 리포트 생성(염기 품질, GC 함량, 깊이) |
| Trimmomatic | 저품질 염기 및 어댑터 제거 |
| ComBat / ComBat-ref | 배치 효과 보정 |
| SVA | 측정되지 않은 잡음 변수(배치 등) 탐지 및 제거 |

## 2. 유전체 (Genomics)

| 도구 | 기능 | 한계 |
|---|---|---|
| GATK, HaplotypeCaller | SNP·소규모 indel 검출의 표준 | 계산 자원 부담이 큼 |
| MuTect2 | tumor-normal 쌍 기반 체세포 변이 검출 | |
| VarScan, FreeBayes, Strelka, LoFreq, Platypus | 고감도 변이 검출 | 필터링 부담이 큼 |
| DeepVariant | 딥러닝 기반 변이 검출 | |
| ANNOVAR, SnpEff | 변이 기능 주석 | |
| CNVkit, Control-FREEC, ExomeCNV | 복제수 변이(CNV) 검출 | 시퀀싱 깊이에 민감, 위양성 발생 |
| FusionCatcher, STAR-Fusion | RNA-seq 기반 융합 유전자(예: ALK) 검출 | |

## 3. 전사체 (Transcriptomics)

| 구분 | 도구 | 기능 |
|---|---|---|
| 정렬·정량 | STAR, HISAT2, HTSeq, RSEM | 정렬 및 리드 카운트 |
| | Salmon, Kallisto | 정렬 없이(alignment-free) 고속 정량 |
| 차등발현 | DESeq2, edgeR | 카운트 기반 DEG 분석 |
| | limma | 마이크로어레이용으로 개발, RNA-seq에도 사용 |
| | Cufflinks, Ballgown | 전사체 수준 발현 분석 |
| 단일세포 | Seurat, Scanpy | 클러스터링 및 세포 이질성 분석 |
| | CellRanger | 10x 단일세포 데이터 처리 |
| | Monocle3 | 궤적(trajectory) 및 계통 분석 |
| | CellBender | 주변 RNA(ambient RNA) 제거 |
| | scVI | 딥러닝 기반 보정(imputation) 및 클러스터링 |
| | Scissor | 단일세포 데이터를 생존 등 임상 표현형과 연결 |
| | dyngen / scRNASeqDB | 단일세포 시뮬레이션 / 데이터베이스 |
| ncRNA | miRDeep2, Infernal, snoSeeker, lncRNAtor | 비암호화 RNA 식별 |

- 한계: 저발현 유전자 정량 부정확, 단일세포 dropout과 잡음으로 세포 유형 주석이 어려움.

## 4. 단백체 (Proteomics)

| 구분 | 도구 | 기능 |
|---|---|---|
| 식별·정량 | MaxQuant, Skyline, Proteome Discoverer, MSFragger | MS 기반 단백질 및 PTM 정량 |
| | OpenMS, PeptideShaker, Trans-Proteomic Pipeline | 오픈소스 펩타이드 식별 |
| | MS-DIAL, DIA-NN | 고처리량 DIA 분석 |
| | DeepNovo | 딥러닝 기반 de novo 펩타이드 서열 분석 |
| 통계 | Perseus, limma/edgeR | 차등 분석 및 위발견 통제 |
| 상호작용 | STRING, Cytoscape, BioGRID, IntAct | PPI 네트워크 구축 및 시각화 |
| PTM | PhosphoSitePlus, PTMScan, MODa | PTM 카탈로그 및 분석 |
| 구조 | AlphaFold, I-TASSER, MODELLER, PyMOL | 구조 예측 및 시각화 |

- 한계: 저농도 단백질 검출이 어렵고 스펙트럼 라이브러리 품질에 의존함.

## 5. 후성유전체 (Epigenomics)

| 구분 | 도구 | 기능 |
|---|---|---|
| DNA 메틸화 | Bismark | 바이설파이트 리드 정렬 및 메틸화 호출 |
| | MethylKit, DSS, Bis-SNP, MethylSig, BSmooth | 차등 메틸화 분석 |
| | EpiDISH | 메틸화 데이터 세포 구성 역추정(deconvolution) |
| 크로마틴 | MACS | ChIP-seq/ATAC-seq 피크 검출 |
| | SICER | 넓은 히스톤 변형 영역 검출 |
| | ChIPseeker, HMMRATAC | 피크 주석, ATAC-seq 분석 |
| 히스톤 | diffReps, RSEG, ChromHMM | 차등 히스톤 변형, 크로마틴 상태 분류 |

- 한계: 반복 영역에서 메틸화 호출이 부정확하고, 저신호 데이터에서 피크와 잡음을 구분하기 어려움.

## 6. 대사체 (Metabolomics)

| 구분 | 도구 | 기능 |
|---|---|---|
| 전처리·정량 | XCMS, MZmine, OpenMS, MetaboAnalyst | 피크 검출, 머무름 시간 보정, 정규화 |
| 동정 | MetFrag | in silico 단편화로 MS/MS 매칭 |
| | GNPS | MS/MS 데이터 공유 및 분자 네트워킹 |
| 경로 | KEGG, HMDB, Reactome, MSEA, Pathway Commons | 대사 경로 매핑 및 농축 분석 |
| 지질체 | LipidSearch, LIMSA, LipidBlast | 지질 동정 및 정량 |
| 통계 | limma, glmnet, SPSS, SAS | PCA, PLS-DA 등 다변량 분석 |

- 한계: 스펙트럼 라이브러리가 제한적이고 m/z 중첩으로 동정이 어려움.

## 7. 멀티오믹스 통합

| 도구 | 기능 |
|---|---|
| MOFA+ | 비지도 요인분석으로 다층 데이터 통합 |
| mixOmics | 특징 선택 및 다중 데이터 통합(R) |
| iCluster / iClusterPlus | 잠재변수 기반 통합 클러스터링으로 아형 발굴 |
| SNF | 오믹스별 유사도 네트워크를 합의 네트워크로 융합 |
| netboxr | PPI 네트워크와 유전체 정보를 결합해 모듈 탐색 |
| Sangerbox 3 | 웹 기반 통합 분석(생존, 농축, 멀티오믹스) |
| Galaxy | 워크플로 기반 통합 분석 플랫폼 |

- 한계: 계산 부담이 크고, 계층 간 상관을 해석하기 어려움.

## 8. 경로 및 네트워크 분석

| 도구 | 기능 |
|---|---|
| GSEA | 유전자 집합 농축 분석 |
| DAVID | 기능 주석 및 농축 |
| Reactome, KEGG | 큐레이션된 경로 데이터베이스 |
| IPA | 상용 경로 및 인과 네트워크 분석 |
| clusterProfiler | R 기반 농축 분석 및 시각화 |
| Metascape | 다중 DB 통합 농축 분석 |
| GeneMANIA | 공발현·상호작용 기반 유전자 기능 예측 |
| NetPath | 암 신호전달 경로 큐레이션 |
| Cytoscape (+ClueGO, BiNGO) | 네트워크 시각화 및 농축 플러그인 |

- 한계: 일반화된 경로에 의존하므로 조직·조건 특이적 경로를 놓칠 수 있음.

## 9. 바이오마커 발굴 알고리즘 및 AI/ML

| 접근 | 대표 도구 | 용도 |
|---|---|---|
| 특징 선택 | Lasso, Elastic Net, 유전 알고리즘(DEAP, GAlib) | 고차원 데이터에서 예측 변수 선별 |
| 지도학습 | scikit-learn, XGBoost, LightGBM, LIBSVM | 아형 분류, 예후 예측 |
| 앙상블 | Random Forest, Gradient Boosting, Stacking | 견고한 예측 및 특징 중요도 산출 |
| 비지도·차원축소 | k-means, DBSCAN, 계층적 군집, PCA, t-SNE, UMAP | 환자 군집화, 신규 아형 탐색 |
| 딥러닝 | TensorFlow, Keras, PyTorch, Caffe | 오믹스 및 병리 이미지 분석 |
| GNN | DGL, PyTorch Geometric | 유전자 상호작용 그래프 모델링 |
| 전이학습 | Keras, PyTorch | 소규모 데이터에 사전학습 모델 적용 |
| 연합학습 | TensorFlow Federated, PySyft | 데이터 이동 없이 기관 간 공동 학습 |
| 설명가능 AI | SHAP, LIME | 예측 근거 제시 |
| 베이지안 네트워크 | PyMC3, Netica | 확률적 관계 및 불확실성 모델링 |
| 강화학습 | OpenAI Gym, TF Agents | 시계열 치료 전략 최적화 |
| AutoML | Google AutoML, H2O.ai, Auto-sklearn | 모델 선택 자동화 |
| NLP | spaCy, SciSpacy, BERT | 문헌 기반 바이오마커 추출 |
| 통합 플랫폼 | PandaOmics, OmicLearn | AI 기반 표적 및 바이오마커 발굴 |

- 과제: 라벨 데이터 부족과 과적합, 이질적 데이터 통합, 블랙박스 문제로 인한 임상 신뢰 부족.

## 10. 검증 및 생존 분석

| 도구 | 기능 |
|---|---|
| Kaplan–Meier, Cox 비례위험 모형 | 발현과 OS·PFS 연관 분석 |
| survminer (R) | KM 곡선 및 Cox 모형 시각화 |
| SurvExpress | 발현 기반 위험 층화 및 외부 코호트 검증 |
| GEPIA | TCGA와 GTEx 발현 비교 및 생존 분석 |
| TIMER | 면역세포 침윤을 반영한 생존 분석 |
| OncoLnc | TCGA mRNA·miRNA·lncRNA 생존 분석 |
| PrognoScan | 예후 메타분석 |
| TCGAbiolinks (R) | TCGA 데이터 재현성 있는 접근 및 분석 |

- 단계: in silico 검증(TCGA, GEO), 분석적 검증(교차검증), 임상적 검증(후향·전향 임상시험) 순으로 진행함.

## 11. 암 특화 도구

| 구분 | 도구 |
|---|---|
| 암 유전체·지식베이스 | cBioPortal, GEPIA, OncoKB, TIMER |
| 약물 감수성 | GDSC, PRISM Repurposing, CellMiner, PharmacoDB |
| 면역 침윤 추정 | CIBERSORT, xCell, EPIC, TIMER |

- 한계: 공개 데이터에 의존하므로 희귀 변이와 인종 특이 정보가 부족함. 세포주 데이터는 실제 반응과 차이가 있음.

## 12. 공개 데이터베이스

| 분야 | 데이터베이스 |
|---|---|
| 암 유전체 | TCGA, ICGC, COSMIC, GDC, Cancer Mutation Census, ExAC |
| 전사체 | GEO, ArrayExpress |
| 단백체 | PRIDE, PeptideAtlas, GPMDB, MassIVE, PASSEL, SRMAtlas, Panorama |
| 대사체 | MetaboLights, HMDB |
| 통합 | cBioPortal, UCSC Xena |
| 접근 통제 | dbGaP |

## 13. 클라우드 및 워크플로

- Galaxy, DNAnexus, Seven Bridges, FireCloud: 대규모 분석 워크플로 플랫폼
- AWS, Google Cloud, Azure: 확장형 연산 인프라
- REDCap, OpenClinica: 임상 데이터 수집 및 분자 데이터 연계

## 결론 및 과제

- 데이터 통합: 오믹스 간 구조와 척도가 달라 표준화가 부족함.
- 계산·저장: TB 단위 데이터를 처리하려면 HPC가 필요하고, 다중검정에 따른 위양성 위험이 있음.
- 임상 전환: 대규모 검증 코호트가 부족하고 규제 비용이 큼.
- 윤리: 비식별화의 한계, 동적 동의, 알고리즘 편향 문제가 있음. 연합학습과 공정성 고려 알고리즘이 대응 방안으로 제시됨.
- 향후 방향: 멀티오믹스와 AI의 결합, 단일세포·공간 오믹스 확대, GA4GH·ELIXIR 기반 데이터 공유 표준화.
