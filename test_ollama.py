import httpx

OLLAMA_BASE_URL = "http://localhost:11434/v1"
OLLAMA_MODEL = "llama3"

def query_llm(prompt):
    url = f"{OLLAMA_BASE_URL}/chat/completions"
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = httpx.post(url, json=payload, eout=90)
    print(response.text)

query_llm("Hello, Ollama! Are you running?")