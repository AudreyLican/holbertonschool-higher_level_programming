#!/bin/mysql
-- lists all records of second_table of DB hbtn_0c_0
-- display score and name, except rows without name value,
-- ordered by DESC score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;