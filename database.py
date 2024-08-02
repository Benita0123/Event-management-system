import mysql.connector

def get_data():
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Benita@3216",
        database="event_manager"
    )
    
    # Create a cursor object
    mycursor = mydb.cursor()
    
    # Execute query to get data from 'events' table
    mycursor.execute("SELECT * FROM events")
    events_result = mycursor.fetchall()
    
    # Execute query to get data from 'user' table
    mycursor.execute("SELECT * FROM user")
    user_result = mycursor.fetchall()
    
    # Close the database connection
    mydb.close()
    
    # Return both results as a tuple
    return events_result, user_result
