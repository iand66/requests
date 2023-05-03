import requests

payload = {"name":"Jeanette","age":59}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.json())

payload = {"name":"Ian","age":56}
response = requests.put("https://httpbin.org/put", data=payload)
print(response.json())

payload = {"name":"Pedro"}
response = requests.patch("https://httpbin.org/patch", data=payload)
print(response.json())