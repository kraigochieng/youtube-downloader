from flask import Flask, request, jsonify, json
from flask_cors import CORS

from src.download_media import downloadMedia
app = Flask(__name__)

CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.post('/api/media/')
def getMedia():
        request_data = request.json
        url = request_data['url']
        media = downloadMedia(url)
        return (media)

if __name__ == "__main__":
    app.run(debug= True)

