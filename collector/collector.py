import json
import random
import time
from datetime import datetime
import docker

DATA_FILE = "/data/monitoring.json"

client = docker.from_env()

while True:
    containers = []

    for container in client.containers.list(all=True):
        containers.append({
            "name": container.name,
            "status": container.status,
            "image": container.image.tags[0] if container.image.tags else "unknown"
        })

    data = {
        "cpu": f"{random.randint(10, 90)}%",
        "memory": f"{random.randint(20, 95)}%",
        "disk": f"{random.randint(30, 80)}%",
        "status": "Running",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "containers": containers
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("Monitoring data updated with container information")
    time.sleep(5)