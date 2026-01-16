# 💻 External Hardware Reference: Apple M5 vs NVIDIA RTX 4080

본 문서는 Apple M5 32GB 시스템과 일반적인 PC 환경(NVIDIA RTX 4080) 간의 성능 차이를 비교 분석하고, <strong>PCIe 인터페이스 및 메모리 한계</strong>가 LLM 성능에 미치는 영향을 기술적으로 추적합니다.

---

## 1. ⚙️ 비교 시스템 제원 (Comparative Specs)

| 항목 | Apple Silicon (M5) | External PC (RTX 4080) |
| :--- | :--- | :--- |
| <strong>프로세서</strong> | Apple M5 Chip (10-Core) | Intel Core i5-9600K |
| <strong>메모리(VRAM)</strong> | <strong>32GB Unified Memory</strong> | <strong>16GB GDDR6X VRAM</strong> |
| <strong>시스템 메모리</strong> | (통합 메모리 사용) | 64GB DDR4 System RAM |
| <strong>대역폭 (Core)</strong> | <strong>153.6 GB/s</strong> (Unified) | 736 GB/s (GPU Only) |
| <strong>버스(Interconnect)</strong> | On-Die (Zero Latency) | <strong>PCIe 3.0 x16</strong> (Limit) |

---

## 2. 📊 벤치마크 데이터: DeepSeek-R1 (14B)

동일한 모델인 `deepseek-r1:14b`를 사용하여 두 시스템의 처리 속도를 대조합니다.

| 측정 지표 | Apple M5 32GB | RTX 4080 (16GB VRAM) | 차이 |
| :--- | :---: | :---: | :---: |
| <strong>생성 속도 (Token Gen)</strong> | 13.74 t/s | <strong>63.6 t/s</strong> | <strong>GPU 압승 (+363%)</strong> |
| <strong>입력 분석 (P-Eval)</strong> | 65.7 t/s | <strong>3.1 t/s</strong> | <strong>Apple M5 압승 (+2,019%)</strong> |

---

## 3. 🔍 기술적 분석 (Scientific Audit)

### ① 생성 속도 (Token Generation): GPU VRAM의 위력
RTX 4080의 <strong>63.6 t/s</strong>는 Apple M5를 압도합니다. 14B 모델의 가중치(VRAM 점유 약 9~11GB)가 NVIDIA GPU의 <strong>736GB/s 초고속 메모리</strong>에 완전히 상주할 수 있기 때문입니다. 생성 단계는 대역폭 싸움이며, 이 영역에서는 전용 VRAM을 가진 외장 GPU가 여전히 강력합니다.

### ② 입력 분석 (Prompt Evaluation): PCIe 3.0의 병목 (Bottleneck)
반면, 프롬프트 분석 단계에서 RTX 4080 기반 시스템은 <strong>3.1 t/s</strong>라는 비정상적인 성능 저하를 기록했습니다. 이는 다음과 같은 기술적 이유 때문입니다.

1.  <strong>버스 대역폭 한계 (PCIe 3.0)</strong>: i5-9600K 시스템의 PCIe 3.0 x16 인터페이스는 이론상 15.75GB/s, 실측 대역폭은 그보다 낮습니다.
2.  <strong>System Memory Fallback</strong>: 14B 모델 구동 시 OS 점유 등을 제외하면 16GB VRAM은 매우 빠듯합니다. 특히 프롬프트 분석 단계에서 발생하는 <strong>Activation Tensors(활성화 텐서)</strong>가 VRAM을 초과하여 <strong>느린 시스템 메모리(DDR4)로 오버플로우</strong>될 경우, 데이터 이동 통로인 PCIe 버스에서 극심한 병목이 발생합니다.
3.  <strong>데이터 왕복 지연 (Latent)</strong>: Apple M5는 <strong>통합 메모리(Unified Memory)</strong> 구조로 CPU/GPU 간 데이터 이동이 0에 가깝지만, PC 환경은 CPU RAM -> PCIe -> GPU VRAM 간의 물리적 이동이 필요하며, PCIe 3.0 환경에서는 이 병목이 LLM 연산 성능을 완전히 잠식합니다.

---

## 4. ✅ 최종 평가 및 통찰

*   <strong>RTX 4080 (16GB)</strong>: 모델이 VRAM에 완전히 들어가는 크기(약 12B 이하)에서는 <strong>폭발적인 생성 속도</strong>를 보여줍니다. 하지만 PCIe 3.0 환경이나 VRAM 용량 한계에 부딪히는 순간, 프롬프트 분석 성능이 실사용 불가능한 수준으로 급락합니다.
*   <strong>Apple M5 (32GB)</strong>: 절대적인 생성 속도(t/s)는 GPU에 못 미치지만, <strong>프롬프트 분석 속도가 균형 잡혀 대형 입력(Long Context) 처리 시 훨씬 쾌적</strong>합니다. 특히 통합 메모리의 저지연성 덕분에 하드웨어의 모든 자원을 LLM 연산에 즉각 동원할 수 있는 효율성이 돋보입니다.

<strong>권장사항</strong>: PC에서 AI 환경을 구축한다면 최소 <strong>PCIe 4.0/5.0</strong> 환경과 모델 파라미터 대비 <strong>20% 이상의 여유 VRAM</strong> 확보가 필수적입니다. 반면, Apple Silicon은 이러한 복잡한 병목 고려 없이 <strong>램 용량만 확보되면 최적의 성능</strong>을 일관되게 제공합니다.
