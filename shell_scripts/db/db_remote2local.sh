#!/bin/bash

# 원격 데이터베이스
MYSQL_HOST=""
MYSQL_USER=""
MYSQL_PASSWORD=""

# 로컬 데이터베이스
MYSQL_HOST_LOCAL="127.0.0.1"
MYSQL_USER_LOCAL=""
MYSQL_PASSWORD_LOCAL=""
DATABASE_NAME=""

# 로컬 데이터베이스를 백업
mysqldump -q --column-statistics=0 --host=$MYSQL_HOST_LOCAL --user=$MYSQL_USER_LOCAL --password=$MYSQL_PASSWORD_LOCAL
$DATABASE_NAME > $DATABASE_NAME-$(date +%Y-%m-%d).sql;

# 원격 데이터베이스를 백업
mysqldump -q --column-statistics=0 --host=$MYSQL_HOST --user=$MYSQL_USER --set-gtid-purged=OFF --password=$MYSQL_PASSWORD
$DATABASE_NAME > $DATABASE_NAME.sql;

# 로컬 데이터베이스에 복구
mysql --host=$MYSQL_HOST_LOCAL --user=$MYSQL_USER_LOCAL --password=$MYSQL_PASSWORD_LOCAL $DATABASE_NAME < $DATABASE_NAME.sql