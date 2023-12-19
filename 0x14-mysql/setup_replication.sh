#!/usr/bin/env bash
# setup_replication.sh

# MySQL user credentials
MYSQL_USER="holberton_user"
MYSQL_PASSWORD="Bruce41234554"

# Connect to MySQL and create database and table
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS tyrell_corp;"
mysql -u root -p -e "USE tyrell_corp; CREATE TABLE IF NOT EXISTS nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL);"
mysql -u root -p -e "USE tyrell_corp; INSERT INTO nexus6 (name) VALUES ('Leon');"

# Grant SELECT permissions to holberton_user
mysql -u root -p -e "GRANT SELECT ON tyrell_corp.nexus6 TO '$MYSQL_USER'@'localhost';"
