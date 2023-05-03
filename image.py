import requests

headers = {
    "User-Agent":"HelloWorld/1.1",
    "Accept":"image/png"
}

response = requests.get("https://httpbin.org/image", headers=headers)

with open ("image.png","wb") as f:
    f.write(response.content)