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


# INSERT INTO `markers` (`marker_id`, `marker_name`, `marker_category_id`, `latitude`, `longitude`)
# VALUES (NULL, 'Lodowka Spoleczna Bujwida', '2', '51.11864559716737', '17.068446189474464');