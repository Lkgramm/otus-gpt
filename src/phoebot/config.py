import os

LM_API_URL = os.getenv("LM_API_URL", "http://localhost:1234/v1/chat/completions")
BOT_TOKEN = os.getenv("BOT_TOKEN", "Ваш токен")
