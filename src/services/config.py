from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL')
EMAIL_SMTP_HOST = os.getenv('EMAIL_SMTP_HOST')
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_TO = os.getenv('EMAIL_TO')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')