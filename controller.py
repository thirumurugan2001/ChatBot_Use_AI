from connectAI import *
from helper import *
import re 

# This AzureOpenAIController function is use to Validate the payload data["prompt"] is not empty and string format.
def AzureOpenAIController(data):
    try:
        if "Question" in data:
            if data["Question"] != "":
                return openai(data)
            else:
                return {
                    "message":"Invaild data !",
                    "statusCode":400
                }
        else:
            return {
                "message":"All fields (Question) are required.",
                "statusCode":400
            }
    except Exception as e:
        return {
                "Error":str(e),
                "statusCode":400
            }
        
# This googleSerpController function is use to Validate the payload data["prompt"] is not empty and string format.
def googleSerpController(data):
    try:
        if "Question" in data:
            if data["Question"] != "":
                return get_google_serp_results(data)
            else:
                return {
                    "message":"Invaild data !",
                    "statusCode":400
                }
        else:
            return {
                "message":"All fields (Question) are required.",
                "statusCode":400
            }
    except Exception as e:
        return {
                "Error":str(e),
                "statusCode":400
            }
        
# This getUsersDetailsController function is use to Validate the payload data["userId"] is not empty and string format.
def getUsersDetailsController(data):
    try:
        if "userId" in data and data["userId"] != "":
            if data["userId"] != "":
                return getUsersDetails(data)
            else:
                return {
                    "message":"Invaild data !",
                    "statusCode":400
                }
        else:
            return {
                "message":"All fields (userId) are required.",
                "statusCode":400
            }
    except Exception as e:
        return {
                "Error":str(e),
                "statusCode":400
            }
         
# This signupController function is use to Validate the payload data["name"], data["email"],data["password"] is not empty and string format.
def signupController(data):
    try:
        if  "name" in data and "email" in data  and "password" and data:
            if data["name"] != "" and data["email"] != "" and data["password"] != "":
                email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                if not re.match(email_regex, data["email"]):
                    return {
                        "message":"Invalid email format.",
                        "statusCode":400
                    }
                users_db = getAllUserEmail()
                user_emails = [user[0] for user in users_db]
                if data["email"] in user_emails:
                    return {"message": "Email already registered.", 
                            "statusCode": 400
                    }
                else: 
                    return signup(data)
            else:
                return {
                    "message":"Invaild data !",
                    "statusCode":400
                }
        else:
            return {
                "message":"All fields (email, password, name) are required.",
                "statusCode":400
            }
    except Exception as e:
        return {
                "Error":str(e),
                "statusCode":400
            }
        
# This signupController function is use to Validate the payload data["name"], data["email"],data["password"] is not empty and string format.
def signInController(data):
    try:
        if "email" in data  and "password" and data:
            if data["email"] != "" and data["password"] != "":
                email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                if not re.match(email_regex, data["email"]):
                    return {
                        "message":"Invalid email format.",
                        "statusCode":400
                    }
                else:
                    return signIn(data)
            else:
                return {
                    "message":"Invaild data !",
                    "statusCode":400
                }
        else:
            return {
                "message":"All fields (email, password) are required.",
                "statusCode":400
            }
    except Exception as e:
        return {
                "Error":str(e),
                "statusCode":400
            }
        
        
        
