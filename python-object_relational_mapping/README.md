Python - Object-relational mapping

sudo apt-get install python3-mysqldb - The error you're seeing is because MySQL-python (also known as MySQLdb) is only compatible with Python 2, while you're using Python 3. The mysqlclient package is the Python 3 compatible version.

For task 7:
Need to create database in 7-model_state_fetch_all.sql(refer to file)
then database needs to be repopulated based on these commands:
> cat 7-model_state_fetch_all.sql | mysql -u root -p
> mysql -u root -p < 7-model_state_fetch_all.sql