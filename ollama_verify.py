import json
import argparse
import os

def compare_benchmarks(file1: str, file2: str):
    if not os.path.exists(file1) or not os.path.exists(file2):
        print(f"Error: Files not found. Ensure {file1} and {file2} exist.")
        return

    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    s1 = data1["system_info"]
    s2 = data2["system_info"]

    print(f"\n=== Benchmark Comparison Report ===")
    print(f"System A: {s1['system_id']} ({s1['machine']})")
    print(f"System B: {s2['system_id']} ({s2['machine']})")
    print("-" * 80)
    print(f"{'Model':<20} | {'Metric':<15} | {s1['system_id']:>12} | {s2['system_id']:>12} | {'Diff (%)':>10}")
    print("-" * 80)

    # Create maps for easier lookup
    bench1 = {b["model"]: b for b in data1["benchmarks"]}
    bench2 = {b["model"]: b for b in data2["benchmarks"]}
    
    # All models mentioned in either file
    all_models = sorted(list(set(bench1.keys()) | set(bench2.keys())))

    for model in all_models:
        if model in bench1 and model in bench2:
            b1 = bench1[model]
            b2 = bench2[model]
            
            m1 = b1["metrics"]
            m2 = b2["metrics"]

            # 1. Tokens per second
            tps1 = m1["tokens_per_second"]
            tps2 = m2["tokens_per_second"]
            diff_tps = ((tps2 - tps1) / tps1 * 100) if tps1 > 0 else 0
            
            print(f"{model:<20} | {'Tokens/s':<15} | {tps1:>12.2f} | {tps2:>12.2f} | {diff_tps:>+9.1f}%")

            # 2. Prompt TPS (Neural Engine / Pre-fill speed)
            ptps1 = m1["prompt_tps"]
            ptps2 = m2["prompt_tps"]
            diff_ptps = ((ptps2 - ptps1) / ptps1 * 100) if ptps1 > 0 else 0
            print(f"{'':<20} | {'P-Eval t/s':<15} | {ptps1:>12.1f} | {ptps2:>12.1f} | {diff_ptps:>+9.1f}%")

            # 3. Response Length Verification
            len1 = len(b1["response"])
            len2 = len(b2["response"])
            print(f"{'':<20} | {'Resp Length':<15} | {len1:>12} | {len2:>12} | {((len2-len1)/len1*100 if len1>0 else 0):>+9.1f}%")
        else:
            # Handle models missing in one of the systems
            val1 = f"{bench1[model]['metrics']['tokens_per_second']:>12.2f}" if model in bench1 else "SKIP/FAILED"
            val2 = f"{bench2[model]['metrics']['tokens_per_second']:>12.2f}" if model in bench2 else "SKIP/FAILED"
            print(f"{model:<20} | {'Tokens/s':<15} | {val1:>12} | {val2:>12} | {'N/A':>10}")
        
        print("-" * 80)

    print("\nComparison complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ollama Benchmark Result Verifier")
    parser.add_argument("file_a", help="Path to first benchmark JSON (e.g. benchmark_M4.json)")
    parser.add_argument("file_b", help="Path to second benchmark JSON (e.g. benchmark_M5.json)")
    args = parser.parse_args()

    compare_benchmarks(args.file_a, args.file_b)
