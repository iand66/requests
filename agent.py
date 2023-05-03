import requests

headers = {
    "User-Agent":"HelloWorld/1.1"
}

response = requests.get("https://httpbin.org/user-agent")
print(response.text)

response = requests.get("https://httpbin.org/user-agent", headers=headers)
print(response.text)