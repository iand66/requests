import requests

params = {"name":"Jeanette","age":59}

#response = requests.get("https://httpbin.org/get")
#response = requests.get("https://httpbin.org/get?name=Ian&age=56")
response = requests.get("https://httpbin.org/get", params=params)

#print(response)
#print(response.text)
print(response.json())