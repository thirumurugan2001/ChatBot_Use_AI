import os
from dotenv import load_dotenv
load_dotenv()
from flask import json
from openai import OpenAI
import requests
from helper import dbconnection

# Connect with OpenAI API and get the response.
def openai(req_body):
    try :
        Question=req_body['Question']
        client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=os.environ["GITHUB_TOKEN"],
        )
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "",
                },
                {
                    "role": "user",
                    "content": Question,
                }
            ],
            model="gpt-4o",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )
        output = response.choices[0].message.content
        connection=dbconnection()
        cursor = connection.cursor()
        query = """SELECT userschat FROM usersChat where userId = %s AND is_active = True"""
        cursor.execute(query, (req_body["userId"],))
        users = cursor.fetchone()       
        if users is None:
            chat=[]
            chat.append(Question)
            chat.append(output)
            DumpChat=json.dumps(chat)
            query = """INSERT INTO usersChat (userschat, userid) VALUES (%s, %s)"""
            cursor.execute(query, (DumpChat, req_body["userId"]))
        else:
            chat = json.loads(users[0]) 
            chat.append(Question)
            chat.append(output)
            DumpChat=json.dumps(chat)
            query = """UPDATE usersChat SET userschat = %s WHERE userid = %s"""
            cursor.execute(query, (DumpChat, req_body["userId"]))
        connection.commit()
        cursor.close()
        connection.close() 
        return chat
        
    except Exception as e:
         return {
                "Error":str(e),
                "statusCode":400
            } 

# Connect with Google Search API and get the response.
def get_google_serp_results(req_body):
    try:
        Question=req_body['Question']
        location="United States"
        language="en", 
        num_results=10
        api_key=os.getenv("SERP_API_KEY")
        url = "https://serpapi.com/search"
        params = {
            "q": Question,
            "location": location,
            "hl": language,
            "num": num_results,
            "api_key": api_key
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status() 
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return {
                "Error":str(e),
                "statusCode":400
            }
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return {
                "Error":str(e),
                "statusCode":400
            }

# Connect with the database and get the response.
def getUsersDetails(data):
    try:
        connection=dbconnection()
        cursor = connection.cursor()
        query = """SELECT userschat FROM usersChat where userId = %s AND is_active = True"""
        cursor.execute(query, (data["userId"],))
        users = cursor.fetchone()
        cursor.close()
        connection.close()
        if users is None:
            return "No user found"
        else:
            chat = json.loads(users[0])
            return chat
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return {
                "Error":str(e),
                "statusCode":400
            }
        
# Connect with the database and store the user details.
def signup(data):
    try:
        connection=dbconnection()
        cursor = connection.cursor()
        query = """INSERT INTO users (username, email, passKey) VALUES (%s, %s, %s)"""
        cursor.execute(query, (data["name"], data["email"], data["password"]))
        connection.commit()
        cursor.close()
        connection.close()
        return "User added successfully"
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return {
                "Error":str(e),
                "statusCode":400
            }
        
# Connect with the database and get the response for the signIn.
def signIn(data):
    try:
        connection=dbconnection()
        cursor = connection.cursor()
        query = """select * from users where email = %s and passkey = %s"""
        cursor.execute(query, (data["email"], data["password"]))
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        if len(users) == 0:
            return "Invalid email or password"
        else:
            return "User logged in successfully"
    except Exception as e:        
        print(f"Error: Unable to connect to the database. {e}")
        return {
                "Error":str(e),
                "statusCode":400
            }