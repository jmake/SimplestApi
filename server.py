import time
from pytubefix import YouTube
from pytubefix.cli import on_progress

from flask import render_template
from flask import Flask, jsonify, request

app = Flask(__name__, template_folder='./')  # Specify your template directory here

data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

# GET endpoint to retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# POST endpoint to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify(new_item), 201

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML file

  
if __name__ == '__main__':
    app.run(debug=True)
    
"""

curl.exe https://simplest-rest-api.glitch.me/items

Invoke-RestMethod -Uri "https://simplest-rest-api.glitch.me/items" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"id": 4, "name": "Item 4"}'
"""
