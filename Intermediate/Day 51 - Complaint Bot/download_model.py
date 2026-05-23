from huggingface_hub import hf_hub_download

repo_id = "bartowski/Meta-Llama-3-8B-Instruct-GGUF"
filename = "Meta-Llama-3-8B-Instruct-Q2_K.gguf"

model_path = hf_hub_download(
    repo_id=repo_id,
    filename=filename,
    cache_dir="./model"   # IMPORTANT: local cache folder in repo
)

print("Model cached at:", model_path)