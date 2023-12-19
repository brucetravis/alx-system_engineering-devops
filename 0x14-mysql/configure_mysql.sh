#!/usr/bin/env bash
# configure_mysql.sh

# MySQL user credentials
MYSQL_USER="holberton_user"
MYSQL_PASSWORD="Bruce41234554"

# Drop the user if it exists
mysql -u root -p -e "DROP USER IF EXISTS '$MYSQL_USER'@'localhost';"

# Create user and grant permissions
mysql -u root -p -e "CREATE USER '$MYSQL_USER'@'localhost' IDENTIFIED BY '$MYSQL_PASSWORD';"
mysql -u root -p -e "GRANT REPLICATION CLIENT ON *.* TO '$MYSQL_USER'@'localhost';"

# Check grants
mysql -u $MYSQL_USER -p -e "SHOW GRANTS FOR '$MYSQL_USER'@'localhost'"
