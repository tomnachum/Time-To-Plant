-- create database time_to_plant;
use time_to_plant;
-- CREATE TABLE users(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(255),
--     email VARCHAR(255),
--     phone_number VARCHAR(255)
-- );
-- CREATE TABLE plants(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(255),
--     description VARCHAR(4096),
--     image VARCHAR(255),
--     watering_gaps INT
-- );
CREATE TABLE users_plants(
    user_id INT,
    plant_id INT,
    note VARCHAR(4096),
    PRIMARY KEY (user_id, plant_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (plant_id) REFERENCES plants(id)
);
CREATE TABLE users_notifications(
    user_id INT,
    plant_id INT,
    PRIMARY KEY (user_id, plant_id),
    time_in_UNIX_TIMESTAMP VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (plant_id) REFERENCES plants(id)
);
-- drop TABLE users_notifications
-- drop DATABASE time_to_plant;