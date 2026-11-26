import requests
import logging
import json
import sys

logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

websites = [
    "https://example.com",
    "https://github.com",
    "https://www.google.com",
    "https://nonexistent.invalid"
]

results = []

for url in websites:
    try:
        response = requests.get(url, timeout=5)

        status = response.status_code
        duration = round(response.elapsed.total_seconds(), 2)

        if status != 200:
            health = "ERROR"
        elif response.elapsed.total_seconds() > 2.0:
            health = "WARNING"
        else:
            health = "OK"

    except requests.exceptions.RequestException:
        status = None
        duration = None
        health = "FAILED"

    result = {
        "url": url,
        "status_code": status,
        "response_time": duration,
        "health": health
    }

    results.append(result)

    message = f"{health} | {url} | {duration}s"

    print(message)

    if health in ["ERROR", "FAILED"]:
        logging.error(message)
    elif health == "WARNING":
        logging.warning(message)
    else:
        logging.info(message)

with open("report.json", "w") as file:
    json.dump(results, file, indent=4)

print("Monitoring report generated.")

if any(r["health"] in ["ERROR", "FAILED"] for r in results):
    sys.exit(1)

sys.exit(0)
