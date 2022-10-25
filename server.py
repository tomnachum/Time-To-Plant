# phone_number_id = "101948529390348"  # Phone number ID provided
# access_token = "EAAUg6nCLVA0BAAufzYBqHpInRqX0vi7b0dkVIaNTgRKHf0OaZCNJoJJ5u17YoHPiMPHD6XKIylZAROTmYp5xdwT2BQN5rOkd2DqFwRbuUadSEbKTqdfSMs1pWcILdx5SGkHqy9s6C33HrF1dGekh1yDTZA7JJKHoZALCG8fbHTh0kfS3iOMo7vZCJnNFLO2MnIlPJ3N9by6wC5VmnJxL5ZAixfQ7m0kZAkZD"  # Your temporary access token
# recipient_phone_number = "972545400958"  # Your own phone number

# url = f"https://graph.facebook.com/v14.0/{phone_number_id}/messages"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json",
# }

# data = {
#     "messaging_product": "whatsapp",
#     "to": recipient_phone_number,
#     "type": "template",
#     "template": {
#         "name": "timetoplant",
#         "language": {"code": "en_US"},
#     },
# }

# import json
# import requests


# response = requests.post(url, headers=headers, data=json.dumps(data))
# print(response.ok)
# print(response.status_code)


from fastapi import FastAPI
import requests
import uvicorn
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.responses import FileResponse

from db_manager import add_to_users_test

app = FastAPI()


@app.get("/")
def root():
    return FileResponse("index.html")


@app.get("/sanity")
def sanity():
    return {"message": "Server is up and running in sanity"}


@app.get("/add-test")
def addTest():
    add_to_users_test()
    return "added to users test"


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8010, reload=True)
