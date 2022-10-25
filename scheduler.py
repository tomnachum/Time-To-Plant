from db_manager import get_data_for_whatsapp
from whatsapp_handler import sendMessage
import time

while True:
    data_to_send_on_whatsapp_array = get_data_for_whatsapp()
    for dataUnit in data_to_send_on_whatsapp_array:
        print(
            f"reminder to {dataUnit['user_name']} to irritate his {dataUnit['plant_name']}"
        )
        sendMessage(dataUnit["phone_number"])

    time.sleep(30)
    print("iteration")
