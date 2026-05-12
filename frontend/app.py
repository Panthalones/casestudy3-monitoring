from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "http://api:5001/api/monitoring"

@app.route("/")
def dashboard():
    response = requests.get(API_URL)
    data = response.json()

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)