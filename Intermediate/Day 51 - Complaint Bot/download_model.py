import os
from huggingface_hub import hf_hub_download

os.makedirs("model", exist_ok=True)

model_path = hf_hub_download(
    repo_id="bartowski/Llama-3.1-8B-Instruct-GGUF",
    filename="Meta-Llama-3-8B-Instruct.Q2_K.gguf",
    local_dir="model",
    local_dir_use_symlinks=False
)

print("Model ready at:", model_path)