import json
import requests


PHONE_NUMBER_ID = "101948529390348"
ACCESS_TOKEN = "EAAUg6nCLVA0BAIojuyuhREwbeJpXaRc0UA4dVQqz4xpQkmcqqaPzxzPXpVjDUgWXLn0TMvKunUJy1ZBvS8UYlcMCt5QCbrRpTdgAlwZC9UbK02ZCeghUPvitlbxjMaMjwQDnnWDwuTLqRLd2WVWU2dx5AYnoGorZBO9jOIkz8TN8UbBbePnDYIukSZBGXTKRp186mHf1IPoncREzjVYuZCkI5ggTe4qjgZD"
ISRAEL = "972"
URL = f"https://graph.facebook.com/v14.0/{PHONE_NUMBER_ID}/messages"
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}


def sendMessage(recipient_phone_number: str, user_name: str, plant_name: str):
    data = {
        "messaging_product": "whatsapp",
        "to": ISRAEL + recipient_phone_number[1:],
        "recipient_type": "individual",
        "type": "template",
        "template": {
            "name": "time_ro_plant_only_params",
            "language": {"code": "en_US"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": f"{user_name}"},
                        {"type": "text", "text": f"{plant_name}"},
                    ],
                },
            ],
        },
    }
    response = requests.post(URL, headers=HEADERS, data=json.dumps(data))
    print(response.ok)
    print(response.status_code)
    print(response.content)
