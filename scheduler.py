from db_manager import get_data_for_whatsapp
from whatsapp_handler import sendMessage
import time
import schedule


def sendWhatsappAlert():
    data_to_send_on_whatsapp_array = get_data_for_whatsapp()
    for dataUnit in data_to_send_on_whatsapp_array:
        sendMessage(
            dataUnit["phone_number"],
            dataUnit["user_name"],
            dataUnit["plants_names"][1:],
        )

    return


schedule.every(30).seconds.do(sendWhatsappAlert)

while True:
    schedule.run_pending()
    time.sleep(1)
