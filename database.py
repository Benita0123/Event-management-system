import mysql.connector

def get_data():
 mydb = mysql.connector.connect(host="localhost",user="root",password="Benita@3216",database="event_manager")
 mycursor = mydb.cursor()
 mycursor.execute( "SELECT * FROM events;")
 result = mycursor.fetchall()
 mycursor.execute( "SELECT * FROM user;")
 result = mycursor.fetchall()

 mydb.close()
 return result
