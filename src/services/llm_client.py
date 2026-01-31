import httpx
from .config import OLLAMA_BASE_URL, OLLAMA_MODEL

def query_llm(prompt):
    url = f"{OLLAMA_BASE_URL}/chat/completions"
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = httpx.post(url, json=payload, timeout=90)  # Add timeout here
    return response.json()['choices'][0]['message']['content']