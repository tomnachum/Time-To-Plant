import pymysql
from typing import List
from plant import Plant

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    db="time_to_plant",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")


def add_plants(plants: List[Plant]):
    try:
        with connection.cursor() as cursor:
            values = []
            for plant in plants:
                values.append(
                    f'("{plant.name}", "{plant.description}", "{plant.image}", {plant.watering_gaps})')
            query = f"INSERT ignore into plants(name, description, image, watering_gaps) values{','.join(values)};"
            print(query)
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")


def add_user(user_name: str, email: str, phone_number: str):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT ignore into Users(name, email, phone_number) values('{user_name}', '{email}', '{phone_number}');"
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")


def add_plants_to_user(user_id: int, plants: List[int]):
    try:
        with connection.cursor() as cursor:
            values = []
            for plant_id in plants:
                values.append(f'({user_id}, {plant_id})')
            query = f"INSERT ignore into users_plants(user_id, plant_id) values {','.join(values)};"
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")


def add_notification(user_id, plant_id, time_in_UNIX_TIMESTAMP):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT ignore into users_notifications(user_id, plant_id, time_in_UNIX_TIMESTAMP) values({user_id},{plant_id},{time_in_UNIX_TIMESTAMP});"
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")
