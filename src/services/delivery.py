import aiosmtplib
import asyncio
from .config import EMAIL_SMTP_HOST, EMAIL_FROM, EMAIL_PASSWORD, EMAIL_TO
from telegram import Bot
from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import asyncio
from telegram import Bot
from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from email.message import EmailMessage
from .config import EMAIL_SMTP_HOST, EMAIL_FROM, EMAIL_PASSWORD, EMAIL_TO



# async def send_email(subject, body):
#     message = f"Subject: {subject}\n\n{body}"
#     await aiosmtplib.send(
#         message,
#         hostname=EMAIL_SMTP_HOST,
#         port=587,
#         username=EMAIL_FROM,
#         password=EMAIL_PASSWORD,
#         start_tls=True,
#         sender=EMAIL_FROM,
#         recipients=[EMAIL_TO]
#     )

# 
async def send_email(subject, html_body, text_body=None):
    msg = EmailMessage()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    # Fallback to plain text if not provided
    msg.set_content(text_body or "Your email client does not support HTML.")
    msg.add_alternative(html_body, subtype='html')

    await aiosmtplib.send(
        msg,
        hostname=EMAIL_SMTP_HOST,
        port=587,
        username=EMAIL_FROM,
        password=EMAIL_PASSWORD,
        start_tls=True,
    )

# def send_telegram(message):
#     bot = Bot(token=TELEGRAM_BOT_TOKEN)
#     bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode='Markdown')

# async def send_telegram(message):
#     bot = Bot(token=TELEGRAM_BOT_TOKEN)
#     await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode=None)

# async def send_telegram(message):
#     from telegram import Bot
#     from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

#     bot = Bot(token=TELEGRAM_BOT_TOKEN)
#     max_length = 4000  # Telegram limit is 4096, keep a little buffer

#     # Split the message into chunks
#     for i in range(0, len(message), max_length):
#         chunk = message[i:i+max_length]
#         await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=chunk, parse_mode=None)

# async def send_telegram(message):
#     from telegram import Bot
#     from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

#     bot = Bot(token=TELEGRAM_BOT_TOKEN)
#     max_length = 4000  # Telegram limit is 4096, keep a little buffer
#     for i in range(0, len(message), max_length):
#         chunk = message[i:i+max_length]
#         await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=chunk, parse_mode="Markdown")

async def send_telegram(message):
    from telegram import Bot
    from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    max_length = 4000  # Telegram limit is 4096, keep a little buffer
    for i in range(0, len(message), max_length):
        chunk = message[i:i+max_length]
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=chunk, parse_mode="HTML")