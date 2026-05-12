from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "/data/monitoring.json"

@app.route("/api/monitoring")
def get_monitoring_data():
    with open(DATA_FILE, "r") as file:
        data = json.load(file)

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)