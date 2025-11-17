import requests

from config import settings


def send_tg_message(chat_id, message):
    params = {
        "chat_id": chat_id,
        "text": message,
    }

    response = requests.post(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
        params=params,
    )

    return response.json()
