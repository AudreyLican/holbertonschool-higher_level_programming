#!/bin/mysql
-- lists number of record with same score in second_table
-- diplaying score, sorted by the number of record in DESC
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;