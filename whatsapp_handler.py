import json
import requests


PHONE_NUMBER_ID = "101948529390348"
ACCESS_TOKEN = "EAAUg6nCLVA0BAKS0akRg4WWvqTROlJLqErjyURudeSOCD8gsg6hslLW3enQZBZAKHaFGx7ZCdepOPz90e7Om21D\
    AsOsL63W5z3AnZCjHsgvmEDTjMUbTG9VTaNsvJkoOlGhqFW3mzcbYrxvBrVNYsrNHjQk2o1sVOvBiX7LomT320T5MkkfNxHYXdnEK1pPgR284szqZCywZDZD"
ISRAEL = "972"
URL = f"https://graph.facebook.com/v14.0/{PHONE_NUMBER_ID}/messages"
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}


def sendMessage(recipient_phone_number: str):
    data = {
        "messaging_product": "whatsapp",
        "to": ISRAEL + recipient_phone_number[1:],
        "type": "template",
        "template": {
            "name": "timetoplant",
            "language": {"code": "en_US"},
        },
    }
    response = requests.post(URL, headers=HEADERS, data=json.dumps(data))
    print(response.ok)
    print(response.status_code)
