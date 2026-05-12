import json
import random
import time
from datetime import datetime

DATA_FILE = "/data/monitoring.json"

while True:
    data = {
        "cpu": f"{random.randint(10, 90)}%",
        "memory": f"{random.randint(20, 95)}%",
        "disk": f"{random.randint(30, 80)}%",
        "status": "Running",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("Monitoring data updated")

    time.sleep(5)