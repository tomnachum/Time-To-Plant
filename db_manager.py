import pymysql
from typing import List
from plant import Plant

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="time_to_plant",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)
connection.autocommit(True)

if connection.open:
    print("the connection is opened")


def add_plants(plants: List[Plant]):
    try:
        with connection.cursor() as cursor:
            values = []
            for plant in plants:
                values.append(
                    f'("{plant.name}", "{plant.description}", "{plant.image}", {plant.watering_gaps})'
                )
            query = f"INSERT ignore into plants(name, description, image, watering_gaps) values{','.join(values)};"
            cursor.execute(query)
            connection.commit()
    except:
        print("DB Error")


def add_user(user_name: str, email: str, phone_number: str):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT ignore into Users(name, email, phone_number) values('{user_name}', '{email}', '{phone_number}');"
            cursor.execute(query)
            connection.commit()
    except:
        print("DB Error")


def add_plants_to_user(user_id: int, plants: List[int]):
    try:
        with connection.cursor() as cursor:
            values = []
            for plant_id in plants:
                values.append(f"({user_id}, {plant_id})")
            query = f"INSERT ignore into users_plants(user_id, plant_id) values {','.join(values)};"
            cursor.execute(query)
            connection.commit()
    except:
        print("DB Error")


def add_notification(user_id, plant_id, time_in_UNIX_TIMESTAMP):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT ignore into users_notifications(user_id, plant_id, time_in_UNIX_TIMESTAMP) values({user_id},{plant_id},'{time_in_UNIX_TIMESTAMP}');"
            cursor.execute(query)
            connection.commit()
    except:
        print("DB Error")


def get_all_plants():
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT *
                    FROM plants
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)


def get_data_for_whatsapp():
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT u.name as user_name, p.name as plant_name, u.phone_number 
                    FROM users as u, users_notifications as un, plants as p 
                    WHERE u.id = un.user_id AND un.plant_id = p.id
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)


# test12
def add_to_users_test():
    try:
        with connection.cursor() as cursor:
            query = (
                f'INSERT into users values(2, "matan", "email@gmail.com", "0504448908")'
            )
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            print(result)
    except:
        print("DB Error")


get_data_for_whatsapp()
