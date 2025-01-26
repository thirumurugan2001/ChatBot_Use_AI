import psycopg2 
from dotenv import load_dotenv
load_dotenv()
import os 

# Function to connect to the database
def dbconnection():
    try:
        # Create a connection to the database
        connection = psycopg2.connect(
            dbname=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password= os.getenv("PASSWORD"),
            host= os.getenv("HOST"),
            port= os.getenv("PORT")
        )
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return None

# Function to get all the users email  details
def getAllUserEmail():
    try:
        connection=dbconnection()
        cursor = connection.cursor()
        cursor.execute("""SELECT email FROM users""")
        email = cursor.fetchall()
        cursor.close()
        connection.close()
        return  email
        
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return []


