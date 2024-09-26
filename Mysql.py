# pip install sql-connector-python
import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", password="root", port=3306,database="Joy")
print(myconn)
x=myconn.cursor()
# print(x)
# x.execute("create table first (name varchar(20),age int, gender varchar(10))")
# x.execute("insert into first (name,age) values('Ram',30),('Shyam',25)")

# x.execute("insert into first(genrer) values('M'),('M')")
myconn.commit()
x.execute("select * from first")
for i in x:
    print (i)