#!/bin/mysql
-- lists all records with score >= 10 in second_table
-- display, score and name, ordered by top score
SELECT score, name
FROM second_table
WHERE score >= 10;