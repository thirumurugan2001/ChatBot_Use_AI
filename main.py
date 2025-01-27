#`Flask` is a web framework. It provides tools, libraries, and technologies that allow you to build a web application. `request` is used to get the data from the user. `jsonify` is used to return the response in JSON format.
#`Cross-Origin Resource Sharing` is a mechanism that uses additional HTTP headers to tell browsers to give a web application running at one origin, access to selected resources from a different origin.
#importing all the functions from the controller file.
#`__name__` is a special variable in Python that is used to determine whether a script is being run as the main program or it is being imported as a module.
#`Cross-Origin Resource Sharing` is a mechanism that uses additional HTTP headers to tell browsers to give a web application running at one origin, access to selected resources from a different origin.
from flask import Flask, request, jsonify 
from flask_cors import CORS 
from controller import * 
app = Flask(__name__)
CORS(app)

# This Route is used to the connect the Azure Open AI gpt-4o and implement the 3th tier.
@app.route('/openAi', methods=['POST'])
def openAi():
    try:
        data = request.get_json()
        response = AzureOpenAIController(data)
        return {
            "data":response,
            "statusCode":200
        }
    except Exception as e:
        print(f"Error in Transcribe Summary: {str(e)}")
        return jsonify({
                "Error":str(e),
                "statusCode":500
            }),400
   
# This Route is used to the connect the Google Search API and implement the 3th tier..
@app.route('/google', methods=['POST'])
def google():
    try:
        data = request.get_json()
        response = googleSerpController(data)
        return {
            "data":response,
            "statusCode":200
        }    
    except Exception as e:
        print(f"Error in generate_summary: {str(e)}")
        return jsonify({
                "Error":str(e),
                "statusCode":500
            }),400

# This Route is used to the connect the Sever and implement the 3th tier..
@app.route('/getUsersDetails', methods=['POST'])
def getUsersDetails():
    try:
        data = request.get_json()
        response = getUsersDetailsController(data)
        return {
            "data":response,
            "statusCode":200
        },200
    except Exception as e:
        print(f"Error in generate_summary: {str(e)}")
        return jsonify({
                "Error":str(e),
                "statusCode":500
            }),400
        
# This Route is used to the connect the Google Search API and implement the 3th tier..
@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        response = signupController(data)
        return {
            "data":response,
            "statusCode":200
        },200
    except Exception as e:
        print(f"Error in generate_summary: {str(e)}")
        return jsonify({
                "Error":str(e),
                "statusCode":500
            }),400
             
# This Route is used to the connect the Google Search API and implement the 3th tier..
@app.route('/signIn', methods=['POST'])
def signIn():
    try:
        data = request.get_json()
        response = signInController(data)
        return {
            "data":response,
            "statusCode":200
        },200
    except Exception as e:
        print(f"Error in generate_summary: {str(e)}")
        return jsonify({
                "Error":str(e),
                "statusCode":500
            }),400
     

# This is the main function in which the application runs.
if __name__ == "__main__":
    app.run(debug=True , port="8080",host="0.0.0.0")