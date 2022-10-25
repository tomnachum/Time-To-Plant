from db_manager import get_data_for_whatsapp
from whatsapp_handler import sendMessage
import time

while True:
    data_to_send_on_whatsapp_array = get_data_for_whatsapp()
    for dataUnit in data_to_send_on_whatsapp_array:
        sendMessage(
            dataUnit["phone_number"], dataUnit["user_name"], dataUnit["plant_name"]
        )

    time.sleep(30)
    print("iteration")
