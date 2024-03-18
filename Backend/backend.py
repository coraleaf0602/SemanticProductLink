from flask import Flask, redirect, url_for, render_template, request, session, Response
from database import retrieve
import flask_cors
import requests 
import json 
import os 

app = Flask(__name__)

api_key = os.environ.get("API_KEY")
    
headers = { 
    "Content-Type": "application/json",   
    "Ocp-Apim-Subscription-Key": api_key  
}

with open("request.json","r") as f:
    azure_json = json.loads(f.read())

database = {}
# @app.route("/")
# def home(): 
#     return render_template("basicWebsite.html")


@app.route("/start-task", methods=["POST"])
@flask_cors.cross_origin()
def start_task():   
    post_url = "https://dellsemanticproductlink.cognitiveservices.azure.com/language/analyze-text/jobs?api-version=2022-10-01-preview"
    requests_body = request.get_json()
    azure_json["analysisInput"]["documents"][0]["text"] = requests_body["text"]
    response = requests.post(url=post_url, headers=headers, json=azure_json)
    get_url = response.headers.get('operation-location')

    # You will receive a 202 response indicating that your task has been submitted successfully.
    if response.status_code == 202:
        return {"job":get_url}
    else:
        print(response.text)
        return Response(status=400,response=response.json())
    
@app.route("/get-task",methods=["GET"])
@flask_cors.cross_origin()
def get_task():     
    get_url = request.args.get("job")
    response = requests.get(url=get_url, headers=headers)
    response_body = response.json()
            
    response_status = response_body.get('status')
    
    if response_status == "succeeded":
        categories = []
        entities = response_body['tasks']['items'][0]['results']['documents'][0]['entities']
        for entity in entities:
            categories.append(entity['category'])  
        # Removes duplicates in the list 
        categories = set(categories)
        links = []
        for category in categories:
            row = retrieve(category)
            if (row != None):
                links.append({"category":row[0],"link":row[1],"image":row[2]})
        return {"category_links":links}
    elif response.status_code == 200:
        return Response(status=202,response={"response-status":response_status})
    else:
        return Response(status=400,response={"Unknown error occured"})

if __name__ == "__main__":
    app.run(debug=True)
