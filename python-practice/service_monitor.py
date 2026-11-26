services = [
    {"name": "Frontend", "status": 200, "response": 0.5},
    {"name": "Booking API", "status": 200, "response": 1.2},
    {"name": "Payment API", "status": 500, "response": 0.8},
    {"name": "User API", "status": 200, "response": 3.5}
]

def check_service(service):
    name = service["name"]
    status = service["status"]
    response = service["response"]

    if status != 200:
        print("[ERROR]", name, "is unhealthy")
    elif response > 2.0:
        print("[WARNING]", name, "is slow")
    else:
        print("[OK]", name, "is healthy")


print("--- CloudForge RideLab Monitoring ---")

for service in services:
    check_service(service)
