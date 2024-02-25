from flask import Flask, redirect, url_for, render_template, request, session, jsonify 
import requests 
import json 
import os 
import time 

app = Flask(__name__)

# The endpoint for authenticating your API request.
endpoint = "https://dellsemanticproductlink.cognitiveservices.azure.com/"
project_name = "SemanticProductLink" 
api_version = "2022-10-01-preview"

# unique identifier assigned to the text analysis job
job_id = ""
api_key = os.environ.get("API_KEY")
    
headers = { 
    # This specifies that the request body is in JSON format
    "Content-Type": "application/json",  
    # Remember to change this to an environment variable saved on Mac 
    "Ocp-Apim-Subscription-Key": api_key  
}
# Define the dictionary with categories as keys and lists of links as values
database = {
    # Add more categories and links as needed
}
@app.route("/")
def home(): 
    return render_template("basicWebsite.html")


# Method to call the Azure model 
# https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-named-entity-recognition/quickstart?pivots=rest-api
@app.route("/import", methods=["POST", "GET"])
def importAI():
    
    # This data is not the same as the JSON file used to train the model, 
    # as it does not contain labeled annotations but rather the input text 
    # that the model will process.
    # For example, text data from the knowledge base articles that we're using 
    
    # construct post request 
    # post_url = f"{endpoint}/language/authoring/analyze-text/projects/{project_name}/:import?api-version={api_version}"
    post_url = "https://dellsemanticproductlink.cognitiveservices.azure.com/language/analyze-text/jobs?api-version=2022-10-01-preview"
   
    # Importing the request.json file. The 'text' label hereis not the same 
    # as the JSON file used to train the model,  as it does not contain labeled
    # annotations but rather the input text that the model will process.
    # For example, text data from the knowledge base articles that we're using 
    with open("request.json", "r") as f:
        requests_body = json.load(f)
        
    # Possible error scenarios for this request:
    # 1. The selected resource doesn't have proper permissions for the storage account.
    # 2. The storageInputContainerName specified doesn't exist.
    # 3. Invalid language code is used, or if the language code type isn't string.
    # 4. multilingual value is a string and not a boolean.
    
    # Make POST request to Azure model endpoint 
    response = requests.post(url=post_url, headers=headers, json=requests_body)
    # Check response status code
    print("Response Status Code:", response.status_code)

    # Check response content
    print("Response Content:", response.text)

    # Check response headers
    print("Response Headers:", response.headers)
    
    # In the response headers, extract operation-location. 
    # You can use this URL to query the task completion status and get the results when task is completed.
    get_url = response.headers.get('operation-location')
    print("Operation Location:", get_url)

    # You will receive a 202 response indicating that your task has been submitted successfully.
    if response.status_code == 202:
        task_running = True
        while task_running:
            response = requests.get(url=get_url, headers=headers)
            response_body = response.json()
            
            response_status = response_body.get('status')
            print(response_status)
            
            # Add a small delay to avoid consuming too much CPU
            time.sleep(1)  # Sleep for 1 second
            if response_status == "succeeded":
                task_running = False
                print(response.text)
                # Save the predicted categories into a list of strings 
                # Extract categories
                categories = []
                for entity in response_body['tasks']['items'][0]['results']['documents'][0]['entities']:
                    categories.append(entity['category'])  
                # Removes duplicates in the list 
                categories = list(set(categories))
                print(categories) 
        return render_template("success.html")
    else:
        return render_template("fail.html")
    
      
if __name__ == "__main__":
    app.run(debug=True)
