from flask import Flask, redirect, url_for, render_template, request, session, jsonify 
import requests 
import json 
import os 
import time 

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return f"<p>{test_data}</p>"

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

@app.route("/")
def home(): 
    return render_template("basicWebsite.html")

# Random page on dell to display and integrate - buggy 
@app.route("/dell")
def dell(): 
    return render_template("index.html")

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
    # GET request to get the status of your importing your project
   
    with open("request.json", "r") as f:
        requests_body = json.load(f)
    # Make POST request to Azure model endpoint 
    
    
    # Possible error scenarios for this request:
    # The selected resource doesn't have proper permissions for the storage account.
    # The storageInputContainerName specified doesn't exist.
    # Invalid language code is used, or if the language code type isn't string.
    # multilingual value is a string and not a boolean.
    # if request.method == "POST": 
    print(headers.values())
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
        # duration = 10 # Set the amount of time we want to continously run the get requests for 
        # start_time = time.time() # Get the start time
        task_running = True
        # Run the while loop until the specified duration is reached
        while task_running:
            response = requests.get(url=get_url, headers=headers)
            # Check response status code
            # print("Response Status Code:", response.status_code)

            # # Check response content
            # print("Response Content:", response.text)
            response_body = response.json()
            
            response_status = response_body.get('status')
            print(response_status)
            # # Check response headers
            # print("Response Headers:", response.headers)

            # # Add a small delay to avoid consuming too much CPU
            # time.sleep(1)  # Sleep for 1 second
            if response_status == "succeeded":
                task_running = False
                print(response.text)
                # Save the predicted categories into a list of strings 
                # Extract categories
                categories = []
                for entity in response_body['tasks']['items'][0]['results']['documents'][0]['entities']:
                    categories.append(entity['category'])  
                categories = list(set(categories))
                print(categories) 
        return render_template("success.html")
    else:
        return render_template("fail.html")
    
    
# We don't need this - training the AI 
@app.route("/train", methods=["POST", "GET"])
def train(): 
    # After your project has been imported, you can start training your model.
    # Submit a POST request using the following URL, headers, and JSON body to submit a training job.
    post_url = f"{endpoint}/language/authoring/analyze-text/projects/{project_name}/:train?api-version={api_version}"
    request_body = {
        "modelLabel": "{MODEL-NAME}",
        "trainingConfigVersion": "{CONFIG-VERSION}",
        "evaluationOptions": {
            "kind": "percentage",
            "trainingSplitPercentage": 90,
            "testingSplitPercentage": 10
        }
    }   
    body_json = json.dumps(request_body, indent=4)

    # if request.method == "POST": 
    response = requests.post(url=post_url, headers=headers, json=body_json)
    return (response.status_code)
    # Returns error response 304 
    

if __name__ == "__main__":
    app.run(debug=True)
