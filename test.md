# 🧪 Test Status & Future Roadmap

본 문서는 현재까지 완료된 테스트 항목과 향후 계획, 그리고 환경설정 팁을 정리한 워킹 파일입니다.

---

## 📅 현재 진행 상황 (Updated: 2026.01.21)

*   [x] Apple M4 16GB 기본 벤치마크 완료
*   [x] Apple M5 32GB 비교 벤치마크 완료
*   [x] **RTX 4080 (PCIe 3.0 Bottleneck)** 데이터 통합 완료
*   [x] **LG EXAONE 3.5 32B** 등 대형 모델 구동 테스트 완료
*   [x] 전 문서 <strong>HTML `<strong>` 태그 기반 렌더링 최적화</strong> 완료

---

## 🚀 모델 추천 리스트 (M5 32GB 기반)

32GB 통합 메모리를 활용할 수 있는 최적의 모델 조합입니다.

| 우선순위 | 모델명 | 목적 | 비고 |
| :---: | :--- | :--- | :--- |
| <strong>Tier 1</strong> | <strong>exaone3.5:32b</strong> | 한국어 전문 지식/문서 작성 | 32GB 램의 존재 이유 |
| <strong>Tier 1</strong> | <strong>deepseek-r1:14b</strong> | 코딩/수학/논리 추론 | M5 Neural Accel 수혜 |
| <strong>Tier 2</strong> | <strong>qwen2.5:32b</strong> | 글로벌 정보/다국어 지원 | 안정적인 성능 유지 |
| <strong>Tier 3</strong> | <strong>llama3.1:8b</strong> | 빠르고 가벼운 일반 비서 | 25 t/s 이상의 쾌속 응답 |

---

## 🛠️ 최적화 설정 팁 (Ollama 기준)

1.  <strong>OLLAMA_NUM_PARALLEL</strong>: M5의 10코어 성능을 활용하려면 병렬 처리 옵션을 확인하세요. <strong>동시 2개 이상의 요청</strong> 처리 시 성능 효율이 좋습니다.
2.  <strong>GPU ↔ RAM 대역폭</strong>: Apple Silicon에서 <strong>메모리 사용량이 80%를 넘지 않도록</strong> 관리하십시오. M5 32GB 시스템 기준, <strong>EXAONE 32B</strong> 모델 사용 시 약 8GB의 여유 공간을 유지하는 것이 OS 안정성에 유리합니다.
3.  <strong>Thunderbolt 연결 금지</strong>: 외장 드라이브에서 모델을 로드할 경우 <strong>SSD 읽기 속도(~7.5GB/s)</strong> 차이로 인해 초기 로딩 시간이 크게 발생할 수 있습니다. 가급적 M5 내장 SSD에 모델을 배치하십시오.

---

## 📈 향후 계획 (Next Objectives)

*   [ ] <strong>Llama 4 (출시 예정)</strong> 대응 벤치마크 수행
*   [ ] 모델 양자화(Bit-level)별 속도 하락폭 정밀 측정
*   [ ] <strong>LM Studio / MLX Framework</strong> 기반 최적화 스크립트 작성
*   [ ] 전력 소모(Watt)당 토큰 생성 효율(Efficiency Context) 추가

---

> [!IMPORTANT]
> 본 데이터는 실측치 기반이나 구동 환경(배경 프로세스, 온도 등)에 따라 편차가 발생할 수 있습니다. <strong>기술적 오류나 신규 데이터 업데이트 예고</strong>는 `Managing Git`을 통해 형상 관리되고 있습니다.
