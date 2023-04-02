import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="testroot",
)

mycursor = mydb.cursor()

try:
    mycursor.execute("DROP DATABASE MAC")
except:
    print("No need to delete any database as i doesn't exists")

mycursor.execute("CREATE DATABASE MAC")
