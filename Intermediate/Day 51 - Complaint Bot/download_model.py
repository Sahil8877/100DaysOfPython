import os
from huggingface_hub import hf_hub_download

HF_TOKEN = os.getenv("HF_TOKEN")

os.makedirs("model", exist_ok=True)

model_path = hf_hub_download(
    repo_id="bartowski/Meta-Llama-3-8B-Instruct-GGUF",
    filename="Meta-Llama-3-8B-Instruct.Q2_K.gguf",
    token=HF_TOKEN,
    local_dir="model"
)

print("Model ready at:", model_path)