#!/bin/bash
-- lists all cities contained in DB hbtn_0d_usa
SELECT cities.id, cities.name, states.name 
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY id ASC;