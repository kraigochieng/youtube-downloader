from flask import Flask, request, jsonify, json
from flask_cors import CORS

from src.download_video import downloadVideo
app = Flask(__name__)

CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.post('/api/video/')
def getVideo():
        request_data = request.json
        url = request_data['url']
        video = downloadVideo(url)
        print(video)
        return (video)

if __name__ == "main":
    app.debug = True

