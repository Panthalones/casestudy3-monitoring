import random
import time
from datetime import datetime
import requests
import os

API_URL = os.getenv("API_URL")

while True:
    data = {
        "cpu": f"{random.randint(10, 90)}%",
        "memory": f"{random.randint(20, 95)}%",
        "disk": f"{random.randint(30, 80)}%",
        "status": "Running from Azure Collector",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "containers": []
    }

    response = requests.post(API_URL, json=data, timeout=10)

    print("Sent monitoring data:", response.status_code)
    time.sleep(5)