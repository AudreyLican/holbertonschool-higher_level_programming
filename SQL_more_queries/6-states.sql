-- Active: 1710514689193@@127.0.0.1@3306@hbtn_0d_usa
#!/bin/bash
-- create a new table in MySQL, 2 columns : id attributes: INT, auto indent, PRIMARY KEY, the other name: NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);