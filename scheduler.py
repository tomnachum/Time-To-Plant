from db_manager import get_data_for_whatsapp
from whatsapp_handler import sendMessage
import time
import sched
import schedule

# while True:
#     data_to_send_on_whatsapp_array = get_data_for_whatsapp()
#     for dataUnit in data_to_send_on_whatsapp_array:
#         sendMessage(
#             dataUnit["phone_number"], dataUnit["user_name"], dataUnit["plant_name"]
#         )

#     time.sleep(30)
#     print("iteration")


def sendWhatsappAlert():
    data_to_send_on_whatsapp_array = get_data_for_whatsapp()
    for dataUnit in data_to_send_on_whatsapp_array:
        sendMessage(
            dataUnit["phone_number"], dataUnit["user_name"], dataUnit["plant_name"]
        )
    return


# def job():
#     print("I'm working...")


schedule.every(30).seconds.do(sendWhatsappAlert)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

time.sleep(5)
while True:
    schedule.run_pending()
    time.sleep(1)
