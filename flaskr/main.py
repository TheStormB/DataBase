import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Berke.teksas1",
    database="airportdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM airportdatabase.departuredetails")



for x in mycursor:
    print(x)