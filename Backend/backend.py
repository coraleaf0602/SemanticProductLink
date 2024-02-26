from flask import Flask, redirect, url_for, render_template, request, session, Response
import flask_cors
import requests 
import json 
import os 

link_lookup_table = {"XPS":"https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/xps-laptops",
                     "Inspiron":"https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/inspiron-laptops",
                     "Laptops and 2-in-1 PC": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops",
                     "Monitors": "https://www.dell.com/en-ie/shop/everyday/sac/monitors/everyday-monitors",
                     "Keyboards and Mice": "https://www.dell.com/en-ie/shop/keyboards/ar/8545/keyboard-mice-combos?appliedRefinements=43910",
                     "Docking Stations": " https://www.dell.com/en-ie/shop/docks-and-stands/ar/8408",
                     "Webcams and Video Conferencing":"https://www.dell.com/en-ie/shop/web-cameras/ar/8332",
                      "Desktops":"https://www.dell.com/en-ie/shop/desktop-computers/sc/desktops"
                     }

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
@app.route("/start-task", methods=["POST"])
@flask_cors.cross_origin()
def start_task():   
    post_url = "https://dellsemanticproductlink.cognitiveservices.azure.com/language/analyze-text/jobs?api-version=2022-10-01-preview"
    requests_body = request.get_json()
    # Make POST request to Azure model endpoint 
    response = requests.post(url=post_url, headers=headers, json=requests_body)
    get_url = response.headers.get('operation-location')

    # You will receive a 202 response indicating that your task has been submitted successfully.
    if response.status_code == 202:
        return {"job":get_url}
    else:
        return Response(status=400,response={"error":"invalid JSON"})
    
@app.route("/get-task",methods=["GET"])
@flask_cors.cross_origin()
def get_task():     
    get_url = request.args.get("job")
    response = requests.get(url=get_url, headers=headers)
    response_body = response.json()
            
    response_status = response_body.get('status')
    
    if response_status == "succeeded":
        categories = []
        for entity in response_body['tasks']['items'][0]['results']['documents'][0]['entities']:
            categories.append(entity['category'])  
        # Removes duplicates in the list 
        categories = set(categories)
        links = []
        for category in categories:
            if category in link_lookup_table.keys():
                links.append({category:link_lookup_table[category]})
        return {"category_links":links}
    else:
        return Response(status=202,response={"response-status":response_status})

if __name__ == "__main__":
    app.run(debug=True)
