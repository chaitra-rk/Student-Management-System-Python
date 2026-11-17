import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="newpass280705",
    database="student_db1"
)

print("Connected Successfully!")