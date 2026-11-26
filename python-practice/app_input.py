app_name = input("Enter application name: ")
environment = input("Enter environment: ")
port = input("Enter application port: ")

print("Application:", app_name)
print("Environment:", environment)
print("Port:", port)

print(type(port))
app_name = input("Enter application name: ")
environment = input("Enter environment: ")
port = int(input("Enter application port: "))
response_time = float(input("Enter response time: "))

print("\n--- Application Configuration ---")

print("Application:", app_name)
print("Environment:", environment)
print("Port:", port)
print("Response Time:", response_time)

print("\n--- Data Types ---")

print(type(app_name))
print(type(environment))
print(type(port))
print(type(response_time))
