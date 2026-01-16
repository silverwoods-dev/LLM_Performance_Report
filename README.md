# 🍎 Apple Silicon LLM Benchmark Suite

Apple Silicon 환경(M4, M5)에서 로컬 LLM(Ollama)의 성능을 측정하고 분석하기 위한 벤치마크 툴킷 및 결과 저장소입니다.

## 🚀 프로젝트 개요

이 프로젝트는 2026년 1월 기준 최신 Apple Silicon 칩셋의 성능을 실제 로컬 LLM 추론 환경에서 테스트합니다. 특히 M5 칩의 **153.6 GB/s Unified Memory**와 새롭게 도입된 **Neural Accelerator** 아키텍처가 DeepSeek-R1, EXAONE 3.5 등의 모델 구동에 미치는 영향을 심층 분석합니다.

## 📊 벤치마크 결과 보고서

상세한 비교 분석 결과와 하드웨어 아키텍처에 따른 성능 인사이트는 아래 문서에서 확인하실 수 있습니다.

*   👉 **[Apple Silicon LLM 성능 비교 보고서 (M4 vs M5)](benchmark_report.md)**
*   👉 **[번외: Apple M5 vs. NVIDIA RTX 4080 성능 비교](benchmark_report_etc.md)** (VRAM Memory Wall 분석)
*   👉 **[LLM 답변 품질 및 일관성 비교 분석](benchmark_response_comparison.md)** 📝 (모델별/시스템별 정성 평가)

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
git clone https://github.com/silverwoods-dev/LLM_Performance_Report.git
cd LLM_Performance_Report
uv sync
```

### 3. 스크립트 실행

#### 1) 모델 설치
벤치마크에 필요한 모델들을 자동으로 다운로드합니다.
```bash
python ollama_setup.py
```

#### 2) 성능 측정 (벤치마크)
각 시스템에서 벤치마크를 수행합니다. `--id`는 필수이며, 메모리 제약으로 실행 불가능한 모델은 `--skip`으로 제외할 수 있습니다.

```bash
# M4 16GB 환경 (32B 모델 등 대형 모델 제외)
python ollama_benchmark.py --id M4_16GB --skip exaone3.5:32b qwen2.5:32b

# M5 32GB 환경 (전체 모델 실행)
python ollama_benchmark.py --id M5_32GB
```

#### 3) 결과 비교 및 검증
생성된 두 JSON 파일을 비교하여 성능 향상 수치와 아키텍처 효율성을 분석합니다.
```bash
python ollama_verify.py benchmark_M4_16GB.json benchmark_M5_32GB.json
```

## ⚖️ 라이선스
이 프로젝트는 MIT License를 따릅니다.
