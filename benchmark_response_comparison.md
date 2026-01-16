# 🤖 Qualitative Evaluation: DeepSeek-R1 vs EXAONE 3.5

본 문서는 수치상의 벤치마크를 넘어, 한국어 처리 능력 및 실제 답변의 품질을 심층 비교한 결과입니다. 하드웨어 사양(Apple M5 32GB)을 최대한 활용할 수 있는 모델을 선정하기 위한 가이드를 제공합니다.

---

## 1. 📋 모델 프로필 (Model Profiles)

| 모델명 | 특징 | 개발사 | 추천 용도 | 한국어 성능 |
| :--- | :--- | :--- | :--- | :---: |
| <strong>DeepSeek-R1 (14B)</strong> | 오픈소스 최강 추론 | DeepSeek | 논리, 수학, 코딩 | <strong>B+</strong> |
| <strong>EXAONE 3.5 (7.8B)</strong> | 가벼운 고성능 | LG AI Research | 일상 대화, 요약 | <strong>A+</strong> |
| <strong>EXAONE 3.5 (32B)</strong> | 대규모 한국어 특화 | LG AI Research | <strong>전문 분석, 작문</strong> | <strong>S (Tier 0)</strong> |

---

## 2. 🔍 실제 답변 품질 비교 (Qualitative Analysis)

### ① 한국어 문맥 이해 및 표현력
*   <strong>DeepSeek-R1 (14B)</strong>: 추론 능력이 매우 뛰어나 복잡한 질문에 대한 논리적 전개는 훌륭합니다. 하지만 <strong>한국어 문장 끝처리가 부자연스럽거나 전형적인 번역 투</strong>가 나타나는 경우가 종종 발견됩니다.
*   <strong>EXAONE 3.5 (32B)</strong>: 한국어 데이터 학습량이 압도적입니다. 신조어, 관용구, <strong>한국적 상황(법률, 문화 등)</strong>에 대한 질문 시 가장 자연스럽고 풍부한 답변을 제공합니다. 32GB 메모리 환경에서 구동 가능한 가장 강력한 모델입니다.

### ② 추론 프로세스 (Chain-of-Thought)
*   <strong>DeepSeek-R1</strong>: 답변 전 `<think>` 태그 내에서 스스로 논리를 점검하는 과정이 매우 정교합니다. 단계별 사고가 필요한 <strong>기술적 문제 해결</strong>에 강점을 보입니다. Apple M5의 <strong>Neural Accelerator</strong> 덕분에 이 사고 과정(P-Eval)이 지연 없이 즉각적으로 표시됩니다.
*   <strong>EXAONE 3.5</strong>: 사고 과정 노출보다는 <strong>완성된 결과값의 품질</strong>에 집중합니다. 속도와 품질의 밸런스가 뛰어나 채팅 기반 비서용으로 적합합니다.

---

## 3. 💡 성능 대비 경험 (T/S vs Quality)

벤치마크 수치(`t/s`)가 높다고 해서 반드시 좋은 경험을 제공하는 것은 아닙니다.

1.  <strong>EXAONE 3.5 7.8B (25.9 t/s)</strong>: <strong>경이로운 속도</strong>를 보여주지만, 복잡한 철학적 질문이나 고도의 코딩 작업 시 답변의 깊이가 얕아지는 경향이 있습니다.
2.  <strong>EXAONE 3.5 32B (6.35 t/s)</strong>: 속도는 다소 느리게 느껴질 수 있으나, <strong>답변의 수준이 인간 전문가에 가장 근접</strong>합니다. Apple M5 32GB 시스템의 진정한 가치는 이 모델을 지연 없이 돌릴 수 있다는 점에 있습니다.
3.  <strong>DeepSeek-R1 14B (13.7 t/s)</strong>: "똑똑한 AI"를 체감하기에 가장 적절한 속도와 지능의 지점에 위치해 있습니다.

---

## 4. 🏆 최종 모델 추천 (Final Verdict)

*   <strong>속도가 가장 중요하다면</strong>: <strong>EXAONE 3.5 7.8B</strong> (채팅 응답이 즉각적임)
*   <strong>논리적 문제 해결이 필요하다면</strong>: <strong>DeepSeek-R1 14B</strong> (사고 과정 가시성 우수)
*   <strong>한국어 전문 작업/창작이 목적이라면</strong>: <strong>EXAONE 3.5 32B</strong> (32GB 환경 필수 추천)

> [!NOTE]
> <strong>M5 32GB 시스템 최적화 팁:</strong> 
> EXAONE 3.5 32B 모델 구동 시 <strong>시스템 자원을 약 22~24GB 소모</strong>합니다. 브라우저 탭을 많이 열어두지 않은 상태에서 최상의 성능이 발휘됩니다.
