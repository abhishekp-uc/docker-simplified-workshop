DROP DATABASE IF EXISTS ieee_project_application;
CREATE DATABASE IF NOT EXISTS ieee_project_application;
USE ieee_project_application;

SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    cell_phone VARCHAR(15),
    age INT DEFAULT NULL,
    PRIMARY KEY (id)
);

INSERT INTO users
    (first_name, last_name, cell_phone, age)
VALUES
    ('Linus', 'Trovaldus', '+91-1234567890', 19),
    ('Dennis', 'Richie', '+91-8596471350', 21);

CREATE TABLE news_articles(
    id INT NOT NULL AUTO_INCREMENT,
    title TEXT NOT NULL,
    page_no INT NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY (id)
);