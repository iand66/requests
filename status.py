import requests

response = requests.post("https://httpbin.org/status/200")
print(response.status_code)

response = requests.post("https://httpbin.org/status/404")
#print(response.status_code)

if response.status_code == requests.codes.not_found:
    print("Page Not Found")
else:
    print(response.status_code)