mysql -u root -p123456 -h 0.0.0.0 -P2000 -e "CREATE DATABASE dvwa;"
mysql -u root -p123456 dvwa -h 0.0.0.0 -P2000 < data-dump.sql