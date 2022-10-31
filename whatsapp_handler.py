import json
import requests
import random


PHONE_NUMBER_ID = "101948529390348"
ACCESS_TOKEN = "EAAUg6nCLVA0BACswWOvIVMypouXdCGjfZBNw5kerpXb1SXUA3n2pqcIzZCmxslqv3fW4GKZB6ZCBvfDpm9flzXgkHDnZCawSGcDnSiu4H9f1DgCy33WdelupAiyNXjjhq5aKMnoVl4joadaBJ1dIo9Qm7bmkG6j7nEI9ZA4OMTBDAbt26umQcZCffvZBZB4bOP0YoQViXMxYH4gZDZD"
ISRAEL = "972"
URL = f"https://graph.facebook.com/v14.0/{PHONE_NUMBER_ID}/messages"
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}
IMAGES_IDS = ["1480842059102903", "3072135316265375"]


def sendMessage(recipient_phone_number: str, user_name: str, plant_name: str):
    data = {
        "messaging_product": "whatsapp",
        "to": ISRAEL + recipient_phone_number[1:],
        "recipient_type": "individual",
        "type": "template",
        "template": {
            "name": "time_to_plant_media",
            "language": {"code": "en_US"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {"type": "image", "image": {"id": random.choice(IMAGES_IDS)}}
                    ],
                },
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
