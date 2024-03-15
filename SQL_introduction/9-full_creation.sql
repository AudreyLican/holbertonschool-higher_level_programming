#!/bin/mysql
-- Create a new table and insert new records
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table SET id = '1', name = 'John', score = '10';
INSERT INTO second_table SET id ='2', name = 'Alex', score ='3';
INSERT INTO second_table SET id ='3', name = 'Bob', score ='14';
INSERT INTO second_table SET id ='4', name = 'George', score ='8';