import ollama
import time
import json
import platform
import argparse
from datetime import datetime
from typing import List, Dict

def get_system_info(system_id: str):
    """Retrieve basic system information."""
    return {
        "system_id": system_id,
        "os": platform.system(),
        "os_version": platform.mac_ver()[0] if platform.system() == "Darwin" else platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "timestamp": datetime.now().isoformat()
    }

def run_benchmark(models: List[str], prompt: str, system_id: str):
    results = {
        "system_info": get_system_info(system_id),
        "benchmarks": []
    }
    
    print(f"\n[{system_id}] Benchmarking {len(models)} models...")
    print(f"Prompt: {prompt}")
    print(f"{'Model':<25} | {'Load(s)':<8} | {'P-Eval':<8} | {'Eval t/s':<10}")
    print("-" * 60)
    
    for model in models:
        try:
            # Force unload/load by setting keep_alive to 0 if needed, 
            # but usually we want to measure standard load.
            response = ollama.generate(model=model, prompt=prompt, stream=False)
            
            # Metrics (nanoseconds to seconds)
            total_duration = response.get('total_duration', 0) / 1e9
            load_duration = response.get('load_duration', 0) / 1e9
            p_eval_count = response.get('prompt_eval_count', 0)
            p_eval_duration = response.get('prompt_eval_duration', 0) / 1e9
            eval_count = response.get('eval_count', 0)
            eval_duration = response.get('eval_duration', 0) / 1e9
            
            tps = eval_count / eval_duration if eval_duration > 0 else 0
            p_tps = p_eval_count / p_eval_duration if p_eval_duration > 0 else 0
            
            print(f"{model:<25} | {load_duration:<8.2f} | {p_tps:<8.1f} | {tps:<10.2f}")
            
            results["benchmarks"].append({
                "model": model,
                "metrics": {
                    "total_duration_s": total_duration,
                    "load_duration_s": load_duration,
                    "prompt_eval_count": p_eval_count,
                    "prompt_eval_duration_s": p_eval_duration,
                    "eval_count": eval_count,
                    "eval_duration_s": eval_duration,
                    "tokens_per_second": tps,
                    "prompt_tps": p_tps
                },
                "response": response.get('response', "")
            })
            
        except Exception as e:
            print(f"{model:<25} | Error: {str(e)}")
            
    # Save to file
    filename = f"benchmark_{system_id}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\nResults saved to {filename}")
    return filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ollama System Benchmark")
    parser.add_argument("--id", required=True, help="System ID (e.g., M4_16GB, M5_32GB)")
    parser.add_argument("--skip", nargs="*", default=[], help="Models to skip (e.g., --skip qwen2.5:32b)")
    args = parser.parse_args()

    # Models from test.md
    target_models = [
        "exaone3.5:7.8b",
        "deepseek-r1:14b",
        "exaone3.5:32b",
        "llama3.1:8b",
        "qwen2.5:32b"
    ]
    
    # Filter out skipped models
    models_to_run = [m for m in target_models if m not in args.skip]
    
    # Prompt for testing
    test_prompt = "인공지능의 미래와 로컬 LLM의 중요성에 대해 3문단으로 설명해줘."
    
    run_benchmark(models_to_run, test_prompt, args.id)
