#install mysqlcoo=nnector from terminal sing pip ( python -m pip install mysql-connector-python )
import mysql.connector
'''Start by creating a connection to the database.
Use the username and password from your MySQL database'''
mydb=mysql.connector.connect(
    host='localhost',
    username='root',
    password='12345678',
    database='py'
)
mycursor=mydb.cursor()

#Creating a Database
mycursor.execute("CREATE DATABASE mydatabase")

# Creating a Table
mycursor.execute('CREATE TABLE stu(id int PRIMARY KEY,name varchar(10))')

#Insert Into Table
sql='INSERT INTO stu(id,name) VALUES(%s,%s)'
val=('01','sandeep')
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount,'row inserted')

#Select From a Table
mycursor.execute('SELECT * FROM stu')
res=mycursor.fetchall()

for x in res:
    print(x)

#selection by using the "WHERE" statement:  
sql = "SELECT * FROM stu WHERE name ='sandeep'"

mycursor.execute(sql)

res = mycursor.fetchall()

for x in res:
  print(x)

#Delete a Table
sql = "DROP TABLE stu"

mycursor.execute(sql)

#for more information about sql connector visit
#https://www.w3schools.com/python/python_mysql_getstarted.asp