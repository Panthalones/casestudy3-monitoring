from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = os.getenv("DATA_FILE", "/tmp/monitoring.json")

@app.route("/api/monitoring", methods=["GET"])
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

@app.route("/api/monitoring", methods=["POST"])
def update_monitoring_data():
    data = request.get_json()

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    return jsonify({"message": "Monitoring data updated"})

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5001)