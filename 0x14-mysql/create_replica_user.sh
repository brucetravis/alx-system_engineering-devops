#!/usr/bin/env bash
# create_replica_user.sh

# MySQL user credentials
MYSQL_USER="holberton_user"
MYSQL_PASSWORD="Bruce41234554"
REPLICA_USER="holb_user"
REPLICA_PASSWORD="@Bruce41234554"

# Grant SELECT privileges on mysql.user to holberton_user
mysql -u root -p -e "GRANT SELECT ON mysql.user TO '$MYSQL_USER'@'localhost';"

# Create replica_user and grant replication privileges
mysql -u root -p -e "CREATE USER '$REPLICA_USER'@'%' IDENTIFIED BY '$REPLICA_PASSWORD';"
mysql -u root -p -e "GRANT REPLICATION SLAVE ON *.* TO '$REPLICA_USER'@'%';"
