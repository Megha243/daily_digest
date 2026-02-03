import requests
from src.services.config import settings


def query_llm(prompt: str) -> str:
    """
    Send a prepared prompt to Ollama and return the response.
    """

    url = f"{settings.OLLAMA_BASE_URL}/api/generate"

    payload = {
        "model": settings.OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(url, json=payload, timeout=120)

    # Helpful debug if Ollama is not reachable
    if response.status_code != 200:
        raise RuntimeError(
            f"Ollama error {response.status_code}: {response.text}"
        )

    return response.json().get("response", "").strip()
