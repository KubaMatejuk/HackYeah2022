#install mysql-connector-python==8.0.29
import mysql.connector

mydb = mysql.connector.connect(
  host="sql7.freesqldatabase.com",
  user="sql7578595",
  password="8PNLIGzmDu",
    database="sql7578595"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM markers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)