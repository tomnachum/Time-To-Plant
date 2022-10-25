from plant import Plant
import db_manager


plants = [
    Plant("Aglaonema", "", "aglaonema.jpg", 3),
    Plant("aloe vera", "", "aloevera.jpg", 3),
    Plant("Diepenbachia", "", "Dieffenbachia_.jpg", 3),
    Plant("Philodendron", "", "pilo.jpg", 3),
    Plant("Calathea", "", "1200px-Calathea_lancifolia_cc5.jpg", 3),
]
db_manager.add_plants(plants)

users = [
    {"name": "Tom", "email": "tom@gmail.com", "phone_number": "0545400958"},
    {"name": "Matan", "email": "matan@gmail.com", "phone_number": "0504448908"},
    {"name": "Adi", "email": "email@gmail.com", "phone_number": "0547659131"},
]

for user in users:
    db_manager.add_user(user["name"], user["email"], user["phone_number"])

users_plants = [
    {"user_id": 1, "plants_id": [1, 2, 3]},
    {"user_id": 2, "plants_id": [2, 3]},
    {"user_id": 3, "plants_id": [1, 3]},
]
for user_plants in users_plants:
    db_manager.add_plants_to_user(user_plants["user_id"], user_plants["plants_id"])

user_notifications = [
    {"user_id": 1, "plant_id": 1, "time_in_UNIX_TIMESTAMP": 12345678},
    {"user_id": 1, "plant_id": 2, "time_in_UNIX_TIMESTAMP": 12345678},
    {"user_id": 1, "plant_id": 3, "time_in_UNIX_TIMESTAMP": 12345678},
    {"user_id": 2, "plant_id": 2, "time_in_UNIX_TIMESTAMP": 12345678},
    {"user_id": 2, "plant_id": 3, "time_in_UNIX_TIMESTAMP": 12345678},
    {"user_id": 3, "plant_id": 1, "time_in_UNIX_TIMESTAMP": 12345678},
    {"user_id": 3, "plant_id": 3, "time_in_UNIX_TIMESTAMP": 12345678},
]
for notification in user_notifications:
    db_manager.add_notification(
        notification["user_id"],
        notification["plant_id"],
        notification["time_in_UNIX_TIMESTAMP"],
    )
