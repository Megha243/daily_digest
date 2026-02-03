import smtplib
import requests
import html
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.services.config import settings


def send_email(items):
    """
    Send digest via Email.
    Article titles are clickable and redirect to the original source.
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "📰 Daily Tech Digest"
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = settings.EMAIL_TO

    html_body = "<h2>Daily Tech Digest</h2>"

    for item in items:
        html_body += f"""
        <hr>
        <h3>
            <a href="{item.link}" target="_blank">
                {item.title}
            </a>
        </h3>
        <p><i>Source: {item.source}</i></p>
        <p>{item.summary}</p>
        """

    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.send_message(msg)


def send_telegram(items):
    """
    Send digest to Telegram using HTML parse mode.
    Titles are clickable and redirect to the original article.
    """

    for item in items:
        title = html.escape(item.title)
        summary = html.escape(item.summary)
        source = html.escape(item.source)

        message = (
            f"<b><a href=\"{item.link}\">{title}</a></b>\n"
            f"<i>Source: {source}</i>\n\n"
            f"{summary}"
        )

        requests.post(
            f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
            json={
                "chat_id": settings.TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "HTML",
                "disable_web_page_preview": False,
            },
            timeout=20,
        )
