-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created or existing database
USE hbtn_0d_usa;

-- Create table states if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);