#!/bin/mysql
-- lists all records from table in display : score, name
-- ordered by top score
SELECT score, name
FROM second_table
ORDER BY score DESC;