import ollama
import sys

def setup_models(models: list):
    print("=== Ollama Model Setup ===")
    print(f"Target models: {', '.join(models)}")
    print("Note: This may take a significant amount of disk space (approx. 60GB+).\n")

    # Get local models to skip already downloaded ones
    try:
        local_models = [m.model for m in ollama.list().models]
    except Exception as e:
        print(f"Error connecting to Ollama: {e}")
        return

    for model in models:
        # Check if model exists (exact or with :latest)
        if model in local_models or f"{model}:latest" in local_models:
            print(f"✅ {model} is already installed. Skipping...")
            continue

        print(f"📥 Pulling {model}...")
        try:
            current_digest = ""
            for progress in ollama.pull(model=model, stream=True):
                status = progress.get('status', '')
                digest = progress.get('digest', '')
                
                # Simple progress display
                if digest != current_digest:
                    print(f"\n  [{model}] {status}", end="", flush=True)
                    current_digest = digest
                
                if 'total' in progress and 'completed' in progress:
                    percent = (progress['completed'] / progress['total']) * 100
                    print(f"\r  [{model}] {status}: {percent:.1f}%", end="", flush=True)
                elif status:
                    print(f"\r  [{model}] {status}", end="", flush=True)
            
            print(f"\n✅ Finished pulling {model}")
            
        except Exception as e:
            print(f"\n❌ Error pulling {model}: {e}")
            print("Tip: Check your internet connection or if the model tag is correct at https://ollama.com/library")

if __name__ == "__main__":
    # Models from your benchmark script
    required_models = [
        "exaone3.5:7.8b",
        "deepseek-r1:14b",
        "exaone3.5:32b",
        "llama3.1:8b",
        "qwen2.5:32b"
    ]
    
    setup_models(required_models)
    print("\nAll setup tasks completed. You can now run 'ollama_benchmark.py'.")
