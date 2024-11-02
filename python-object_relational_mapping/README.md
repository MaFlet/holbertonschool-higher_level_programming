Python - Object-relational mapping

sudo apt-get install python3-mysqldb - The error you're seeing is because MySQL-python (also known as MySQLdb) is only compatible with Python 2, while you're using Python 3. The mysqlclient package is the Python 3 compatible version.