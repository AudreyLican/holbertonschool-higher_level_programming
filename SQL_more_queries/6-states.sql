#!/bin/bash
-- create a new table in MySQL, 2 columns : id attributes: INT, auto indent, PRIMARY KEY, the other name: NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);