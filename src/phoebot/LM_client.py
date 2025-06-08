import requests
from .config import LM_API_URL

SYSTEM_PROMPT = {
    "role": "system",
    "content": "Ты — Фиби Буффе из сериала 'Друзья'. Отвечай в её странном, весёлом и немного сумасшедшем стиле."
}

def generate_reply(user_message: str) -> str:
    payload = {
        "messages": [
            SYSTEM_PROMPT,
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.9,
        "max_tokens": 200
    }

    response = requests.post(LM_API_URL, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]
