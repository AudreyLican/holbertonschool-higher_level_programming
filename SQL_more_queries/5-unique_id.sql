#!/bin/bash
-- create a new table in MySQL, 2 columns : id in INT with default to 1 and unique and name
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);