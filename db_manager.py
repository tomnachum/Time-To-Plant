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


def add_plants_to_user(user_id: int, plants: List[int], note=""):
    try:
        with connection.cursor() as cursor:
            values = []
            for plant_id in plants:
                values.append(f'({user_id}, {plant_id}, "{note}")')
            query = f"INSERT ignore into users_plants(user_id, plant_id, note) values {','.join(values)};"
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


def delete_notification(user_id, plant_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
            DELETE FROM users_notifications 
            WHERE user_id={user_id} and plant_id={plant_id};
            """
            cursor.execute(query)
            connection.commit()
    except:
        print("DB Error")


def delete_plant_of_user(user_id, plant_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
            DELETE FROM users_plants 
            WHERE user_id={user_id} and plant_id={plant_id};
            """
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


def get_plant_by_name(plant_name):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT * FROM plants
                    where name='{plant_name}';
                    """
            print(query)
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)


def get_user_plants(user_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT p.id, p.name, p.description, p.image, p.watering_gaps, up.note
                    FROM users_plants as up, plants as p 
                    where up.user_id={user_id} and up.plant_id=p.id;
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
                    SELECT GROUP_CONCAT(concat(' ' ,p.name) ) as plants_names ,u.name as user_name, p.name as plant_name, u.phone_number 
                    FROM users as u, users_notifications as un, plants as p 
                    WHERE u.id = un.user_id AND un.plant_id = p.id 
                    GROUP BY u.name 
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            return result
    except Exception as e:
        print(e)


def get_notifications_of_user(user_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT plant_id
                    FROM users as u JOIN users_notifications as un
                    ON u.id = un.user_id
                    WHERE user_id='{user_id}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["plant_id"] for e in result]
    except Exception as e:
        print(e)


def get_plants_of_user(user_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT plant_id
                    FROM users as u JOIN users_plants as up
                    ON u.id = up.user_id
                    WHERE user_id='{user_id}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["plant_id"] for e in result]
    except Exception as e:
        print(e)


def update_note(user_id, plant_id, note):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    UPDATE users_plants
                    SET note = '{note}'
                    WHERE user_id = {user_id} AND plant_id = {plant_id};
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            return result
    except Exception as e:
        print(e)
