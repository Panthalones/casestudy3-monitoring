from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

API_URL = os.getenv(
    "API_URL",
    "http://api:5001/api/monitoring"
)

@app.route("/")
def dashboard():
    try:
        response = requests.get(API_URL, timeout=5)
        data = response.json()
    except Exception as e:
        data = {
            "cpu": "N/A",
            "memory": "N/A",
            "disk": "N/A",
            "status": f"Error: {e}",
            "last_updated": "N/A",
            "containers": []
        }

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)