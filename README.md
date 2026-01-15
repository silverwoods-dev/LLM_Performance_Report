# 🍎 Apple Silicon LLM Benchmark Suite

Apple Silicon 환경(M4, M5)에서 로컬 LLM(Ollama)의 성능을 측정하고 분석하기 위한 벤치마크 툴킷 및 결과 저장소입니다.

## 🚀 프로젝트 개요

이 프로젝트는 최신 Apple Silicon 칩셋의 성능을 실제 로컬 LLM 추론 환경에서 테스트합니다. 특히 M5 칩에서 새롭게 도입된 **Neural Accelerator** 아키텍처와 **확장된 메모리 대역폭**이 DeepSeek-R1, EXAONE 3.5 등의 모델 구동에 미치는 영향을 심층 분석합니다.

## 📊 벤치마크 결과 보고서

상세한 비교 분석 결과와 하드웨어 아키텍처에 따른 성능 인사이트는 아래 문서에서 확인하실 수 있습니다.

👉 **[Apple Silicon LLM 성능 비교 보고서 (M4 vs M5)](benchmark_report.md)**

---

## 🛠️ 주요 기능

- **자동 벤치마크 스크립트**: Ollama 환경에서 다양한 모델의 Token Generation 및 Prompt Evaluation 속도 측정.
- **환경 검증 도구**: 테스트 전 시스템 사양 및 Ollama 설정 상태 확인.
- **데이터 분석 및 리포팅**: 수집된 벤치를 바탕으로 시각화 및 인사이트 도출.

## 📋 포함 모델
- **DeepSeek-R1** (14B)
- **EXAONE 3.5** (7.8B, 32B)
- **Llama 3.1** (8B)
- **Qwen 2.5** (32B)

## 💻 사용 방법

### 1. 전제 조건
- [Ollama](https://ollama.com/) 설치 및 실행 중이어야 합니다.
- Python 3.12+ 및 `uv` (추천) 설치.

### 2. 설치
```bash
git clone https://github.com/your-username/apple-silicon-llm-bench.git
cd apple-silicon-llm-bench
uv sync
```

### 3. 스크립트 실행
```bash
# 환경 검증
python ollama_verify.py

# 벤치마크 수행
python ollama_benchmark.py
```

## ⚖️ 라이선스
이 프로젝트는 MIT License를 따릅니다.
