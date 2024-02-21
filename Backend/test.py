from flask import Flask, redirect, url_for, render_template, request, session, jsonify 
import requests 
import json 
import os 

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
    return render_template("dellRandomPage.html")

# Method to call the Azure model 
# Scrapping this cuz I realised I was completely misinterpreting what we're doing 
# https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-named-entity-recognition/quickstart?pivots=rest-api
@app.route("/import", methods=["POST", "GET"])
def importAI():
    
    # This data is not the same as the JSON file used to train the model, 
    # as it does not contain labeled annotations but rather the input text 
    # that the model will process.
    # For example, text data from the knowledge base articles that we're using 
    test_data = """Instructions
Need help with setting up a Dell docking station with a laptop? This article provides information about how to connect and set up a Dell docking station with a laptop. You can also find common troubleshooting steps and answers to some frequently asked questions.

Docking stations help provide the modern worker with the best of both worlds, the benefits of a desktop computer without sacrificing the portability of a laptop. You may connect external monitors, Ethernet for reliable connection, USB ports for connecting devices, and a full-sized keyboard and mouse, among other things.

The interface to connect a Dell docking station to a laptop may vary. To learn more about different types of Dell docking stations, see our Guide to Dell Docking Stations.

Expand all | Collapse all
Verify that you are using a compatible docking station with the laptop
Docking stations come with different types of docking interfaces. For example, Dell E-port or D-port, Thunderbolt 3, USB-C, USB 3.0, or WiGig (wireless). It is important to identify if the type of docking interface or port that is available on the computer is compatible with the docking station.

Dell E-port or D-port - Proprietary docking solution for Dell Latitude and Dell Precision E-series. Dell docking stations provide efficient connectivity to all desktop devices and devices with a simple click into the docking station. Available mostly on Dell Latitude laptops and certain Precision mobile workstations.
Thunderbolt 3 - Thunderbolt 3 docking stations link all devices to the laptop using a single USB-C Thunderbolt cable. Extend the traditional USB capabilities with native multi-display video, audio, data, and power delivery (on select Dell laptops) to charge the laptop with a single USB-C cable. The reversible connector is convenient to use USB-C, with no wrong orientation.
DisplayPort over USB-C - USB-C docking station links all devices to the laptop using a single USB-C cable. Extend the traditional USB capabilities with native multi-display video, audio, data, and power delivery (on select Dell laptops) to charge the laptop with a single USB-C cable. The reversible connector is convenient to use USB-C, with no wrong orientation.
USB 3.0 - Universal docking stations work with DisplayLink technology that enables docking features over USB. The universal docking solution enables multiple monitors, audio, Ethernet, and other USB devices to be connected to laptops through USB. Works best with USB 3.0 ports on the laptop.
WiGig (wireless) - WiGig or wireless docking stations work with a laptop that is configured with a WiGig adapter. Only select Dell laptops support WiGig technology."""
    # construct post request 
    # post_url = f"{endpoint}/language/authoring/analyze-text/projects/{project_name}/:import?api-version={api_version}"
    post_url = "https://dellsemanticproductlink.cognitiveservices.azure.com/language/analyze-text/jobs?api-version=2022-10-01-preview"
    # GET request to get the status of your importing your project
    get_url = "https://dellsemanticproductlink.cognitiveservices.azure.com/language/analyze-text/jobs?api-version=2022-10-01-preview"
    # Request body 
    with open("/Users/zhangc/Documents/CS Year 2/Semester 2/CSU22013 Software Engineering Project I /SwEng-Group-14-SemanticProductLink/Training_Data/weijian.json", "r") as f:
        requests_body = json.load(f)

    # Make POST request to Azure model endpoint 
    
    
    # Possible error scenarios for this request:
    # The selected resource doesn't have proper permissions for the storage account.
    # The storageInputContainerName specified doesn't exist.
    # Invalid language code is used, or if the language code type isn't string.
    # multilingual value is a string and not a boolean.
    # if request.method == "POST": 
    response = requests.post(url=post_url, headers=headers, json=requests_body)
    # Check response status code
    print("Response Status Code:", response.status_code)

    # Check response content
    print("Response Content:", response.text)

    # Check response headers
    print("Response Headers:", response.headers)
    if response.status_code == 202:
        return f"<p>Success</p>"
    else:
        print(response.status_code)
        return f"<p>Fail</p>"
    
    # else: 
    #     response = requests.get(url=get_url, headers=headers)
    # return("get method") 

# Querying our model 
# Reference link: https://learn.microsoft.com/en-gb/azure/ai-services/language-service/custom-named-entity-recognition/how-to/call-api?tabs=rest-api#send-an-entity-recognition-request-to-your-model
@app.route("/query", methods=["POST", "GET"])
def query(): 
    
    
    
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
