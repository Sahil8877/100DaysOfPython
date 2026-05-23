import os
import requests

MODEL_PATH = "model/Meta-Llama-3-8B-Instruct.Q2_K.gguf"
URL = "/Users/sahil/.cache/huggingface/hub/models--Sahil8877--complaint-bot-model/snapshots/29931d50805b7c0f707babc00c5370631caa8ac7/Meta-Llama-3-8B-Instruct.Q2_K.gguf"

os.makedirs("model", exist_ok=True)

if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    r = requests.get(URL, stream=True)
    with open(MODEL_PATH, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Download complete")
else:
    print("Model already cached")