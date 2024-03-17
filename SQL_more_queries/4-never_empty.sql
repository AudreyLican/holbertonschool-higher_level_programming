#!/bin/bash
-- create a new table in MySQL, 2 columns : id in INT with default to 1 and name
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);