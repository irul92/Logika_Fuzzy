import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fuzzy_modul1"
)

print("Database berhasil terhubung!")