phone_number_id = "101948529390348"  # Phone number ID provided
access_token = "EAAUg6nCLVA0BAAufzYBqHpInRqX0vi7b0dkVIaNTgRKHf0OaZCNJoJJ5u17YoHPiMPHD6XKIylZAROTmYp5xdwT2BQN5rOkd2DqFwRbuUadSEbKTqdfSMs1pWcILdx5SGkHqy9s6C33HrF1dGekh1yDTZA7JJKHoZALCG8fbHTh0kfS3iOMo7vZCJnNFLO2MnIlPJ3N9by6wC5VmnJxL5ZAixfQ7m0kZAkZD"  # Your temporary access token
recipient_phone_number = "972545400958"  # Your own phone number

url = f"https://graph.facebook.com/v14.0/{phone_number_id}/messages"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

data = {
    "messaging_product": "whatsapp",
    "to": recipient_phone_number,
    "type": "template",
    "template": {
        "name": "timetoplant",
        "language": {"code": "en_US"},
    },
}

import json
import requests


response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.ok)
print(response.status_code)
