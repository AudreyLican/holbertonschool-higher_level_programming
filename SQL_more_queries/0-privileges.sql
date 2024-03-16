#!/bin/bash
-- lists all privileges of the MySQL users in localhost
-- checking user_0d_1 and user_0d_2
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR "user_0d_2"@"localhost";