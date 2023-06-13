from flask import Flask, request, jsonify, json
from flask_cors import CORS

import functions

app = Flask(__name__)

CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.post('/api/media/')
def getMedia():
    request_data = request.json
    url = request_data['url']
    media = functions.getMedia(url)
    return media

@app.post('/api/download-video/')
def downloadVideo():
    request_data = request.json
    url = request_data['url']
    resolution = request_data['resolution']
    functions.downloadVideo(url, resolution)
    return request_data

if __name__ == "__main__":
    app.run(debug= True)

