import requests

websites = [
    "https://example.com",
    "https://github.com",
    "https://www.google.com",
"https://nonexistent.invalid"
]

for url in websites:
    try:
        response = requests.get(url, timeout=5)

        status = response.status_code
        duration = response.elapsed.total_seconds()

        if status != 200:
            print("[ERROR]", url, status)
        elif duration > 2.0:
            print("[WARNING]", url, round(duration, 2), "s")
        else:
            print("[OK]", url, round(duration, 2), "s")

    except requests.exceptions.RequestException as error:
        print("[FAILED]", url, error)
