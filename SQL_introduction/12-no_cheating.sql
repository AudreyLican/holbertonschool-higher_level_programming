#!/bin/mysql
-- change the score orf Bob to 10
-- by only using the name and not ID
UPDATE second_table SET score = '10'
WHERE name = 'Bob';