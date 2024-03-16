from flask import Flask, redirect, url_for, render_template, request, session, Response
import flask_cors
import requests 
import json 
import os 
import sqlite3

link_lookup_table = {"Laptops and 2-in-1 PC": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sc/laptops", 
                    "XPS": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/xps-laptops", 
                    "Latitude": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/latitude-laptops", 
                    "Inspiron": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/inspiron-laptops", 
                    "Vostro": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/vostro-laptops", 
                    "Alienware": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/alienware-laptops",
                    "Precision": "https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/sr/laptops/precision-laptops",
                    "Desktops": "https://www.dell.com/en-ie/shop/desktop-computers/sc/desktops",
                    "OptiPlex": "https://www.dell.com/en-ie/shop/desktop-computers/sr/desktops/optiplex-desktops", 
                    "Monitors": "https://www.dell.com/en-ie/shop/computer-monitors/ar/8605",
                    "Docking Stations": "https://www.dell.com/en-ie/shop/docks-and-stands/ar/5441/docking-stations?appliedRefinements=962", 
                    "Audio": "https://www.dell.com/en-ie/shop/audio/ac/8310", 
                    "Keyboards and Mice":"https://www.dell.com/en-ie/shop/keyboards-mice/ar/6591",
                    "Hard Drives, SSDs and Storage": "https://www.dell.com/en-ie/shop/hard-drives-storage/ar/8496", 
                    "Webcams and Video Conferencing": "https://www.dell.com/en-ie/shop/web-cameras/ar/8332", 
                    "Batteries, Chargers and Power Adapters": "https://www.dell.com/en-ie/shop/pc-accessories/ar/5436/batteries-chargers-power-adapters?appliedRefinements=44426", 
                    "Cables and Adapters": "https://www.dell.com/en-ie/shop/cables/ar/8168/cables-adapters?appliedRefinements=44427",
                    "Security and Protection": "https://www.dell.com/en-ie/shop/security-protection/ar/7664",
                    "Parts, Batteries and Upgrades": "https://www.dell.com/en-ie/shop/parts-batteries-upgrades/ar/7566", 
                    "Wi-Fi and Networking": "https://www.dell.com/en-ie/shop/wifi-and-networking/ar/4011",
                    "Gaming Accessories": "https://www.dell.com/en-ie/shop/gaming-gaming-accessories/ac/6488"
                    }

app = Flask(__name__)
#  after run create_db.py, the database is created 
# conn = sqlite3.connect('eneities.db')
# cursor = conn.cursor()
# command = 'insert into entity (Entity_Name,URL,ImagePath) VALUES (Entity_Name,URLString,ImagePath_String)'
# cursor.execute(command)
# cursor.close()
# conn.close()

api_key = os.environ.get("API_KEY")


headers = { 
    "Content-Type": "application/json",   
    "Ocp-Apim-Subscription-Key": api_key  
}

with open("request.json","r") as f:
    azure_json = json.loads(f.read())

database = {}
@app.route("/")
def home(): 
    return render_template("basicWebsite.html")


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
            if category in link_lookup_table.keys():
                links.append({"category":category,"link":link_lookup_table[category]})
        return {"category_links":links}
    elif response.status_code == 200:
        return Response(status=202,response={"response-status":response_status})
    else:
        return Response(status=400,response={"Unknown error occured"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000) 
    # app.run(debug=True)
