from llama_cpp import Llama
import random

def response(complains, reason):
    response_list = []

    # Randomly selected per tweet to add variety
    # The model picks up on tone well enough with Q4_K_M quantization
    tones = [
        "angry",
        "sarcastic",
        "dramatic",
        "passive aggressive",
        "existential",
        "british humour",
        "chronically online",
        "overreacting"
    ]

    # Load the model once outside the loop
    # Loading inside the loop works but costs ~5 seconds per complaint
    # Q4_K_M is the sweet spot between quality and file size (~4.9GB)
    # Q2_K was tried first but too lossy to follow system prompt instructions reliably
    llm = Llama(
        model_path="model/Meta-Llama-3-8B-Instruct-Q4_K_M.gguf",
        n_ctx=2048,   # Sufficient for short tweet generation, model trained on 8192 but we don't need it
        verbose=False
    )

    for complaint in complains:
        tone = random.choice(tones)

        messages = [
            {
                "role": "system",
                "content": (
                    f"You are a {tone} Twitter user who writes short funny complaint tweets "
                    f"about {reason} conditions. "
                    "Output ONLY the tweet text. "
                    "Mention officials for that region, use hashtags. "
                    "Do not explain anything. "
                    "Do not add headers, notes, or multiple tweets. "
                    "Maximum 1 sentence."
                )
            },
            {
                "role": "user",
                "content": complaint
            }
        ]

        response = llm.create_chat_completion(
            messages=messages,
            max_tokens=60,          # Keeps output within tweet length
            temperature=1.1,        # Slightly above default for creative variety
            top_p=0.9,
            repeat_penalty=1.25,    # Discourages repetitive phrasing common in smaller models
            stop=["\n", "<|eot_id|>"]  # Llama 3 specific stop token + newline to prevent multi-line output
        )

        response_list.append(response['choices'][0]['message']['content'])

    return response_list