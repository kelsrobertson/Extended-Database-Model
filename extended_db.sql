# Singular table in database
CREATE DATABASE extended_contact_db;
USE extended_contact_db;

CREATE TABLE long_contact (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100),
    sex VARCHAR (10),
    dob DATE,
    age INT, 
    email VARCHAR(100)
);

INSERT INTO long_contact (name, surname, sex, dob, age, email) 
VALUES ('Emily', 'Johnson', 'Female', '1995-06-15', 29, 'emily.johnson@gmail.com'),
       ('Michael', 'Smith', 'Male', '1988-12-20', 36, 'michael.smith@gmail.com'),
       ('Alice', 'Thompson', 'Female', '2001-11-05', 22, 'alice.thompson@gmail.com');




SHOW TABLES;


SELECT * FROM long_contact;