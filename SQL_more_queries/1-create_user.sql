#!/bin/bash
-- creates user user_0d_1 with password set to user_0d_1_pwd
-- if user exist script shouldn't fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';