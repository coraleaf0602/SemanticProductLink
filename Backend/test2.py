from flask import Flask, request, jsonify
import requests
import os
import json

api_key = os.environ.get('AZURE_API_KEY') #get API key from machine environment variable

app = Flask(__name__)

endpoint_url = "https://dellsemanticproductlink.cognitiveservices.azure.com/language/authoring/analyze-text/projects/{project_name}/:import?api-version=2022-05-01"
project_name = "test2" #placeholder name

with open("C:/Users/oscar/OneDrive/Documents/Projects/SwEng-Group-14-SemanticProductLink/Training_Data/weijian.json", "r") as file:
  body = json.load(file)

headers = {
    "Ocp-Apim-Subscription-Key": ""  #need to import the api key from an environment variable for security
}

print()
@app.route("/")
def test2(): 

    response = requests.post(url=endpoint_url, headers=headers, json=body)

    if response.status_code == 202:
        return f"<p>Worked successfully (Status Code: {response.status_code})</p>"
    else:
        return f"<p>Error: Did not work (Status Code: {response.status_code})</p>"


if __name__ == '__main__':
    app.run(debug=True)