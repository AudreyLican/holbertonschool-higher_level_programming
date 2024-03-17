#!/bin/bash
-- lists all cities of California in DB hbtn_0d_usa
SELECT id, name FROM cities
WHERE cities.state_id = (
    SELECT id FROM states
    WHERE name = 'California')
ORDER BY id ASC;