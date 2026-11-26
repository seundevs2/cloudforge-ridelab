status_code = 200
response_time = 2.26
max_response_time = 2.0

is_healthy = status_code == 200
is_slow = response_time > max_response_time

print("HTTP Status:", status_code)
print("Response Time:", response_time)
print("Application Healthy:", is_healthy)
print("Application Slow:", is_slow)
