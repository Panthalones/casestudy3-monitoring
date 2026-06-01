from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = os.getenv("DATA_FILE", "/data/monitoring.json")

@app.route("/api/monitoring")
def get_monitoring_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    else:
        data = {
            "cpu": "25%",
            "memory": "50%",
            "disk": "40%",
            "status": "Running in Azure",
            "last_updated": "Azure demo",
            "containers": []
        }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5001)