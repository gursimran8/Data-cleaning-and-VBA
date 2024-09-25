pip install sql-connector-python
import mysql.connector
myconn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port=3306
)

print(mydb)