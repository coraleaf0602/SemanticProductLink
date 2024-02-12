from flask import Flask, redirect, url_for, render_template, request, session, jsonify 
import requests 

app = Flask(__name__)

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

# @app.route("/")
# def hello_world():
#     return f"<p>{test_data}</p>"

@app.route("/")
def predict():
 
    data = "/Users/zhangc/Documents/CS Year 2/Semester 2/CSU22013 Software Engineering Project I /SwEng-Group-14-SemanticProductLink/Training_Data/weijian.json"
    # Make POST request to Azure model endpoint
    url = "https://dellsemanticproductlink.cognitiveservices.azure.com/language/authoring/analyze-text/projects/hello/:import?api-version=2022-10-01-preview"
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": "b3bb51730d9c4d6f92abd3d817d46043"
    }
    response = requests.post(url=url, headers=headers, json=data)

    if response.status_code == 202:
        return f"<p>Labels imported succesfully</p>"
    else:
        return f"<p>Fail</p>"

if __name__ == "__main__":
    app.run(debug=True)
