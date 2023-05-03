import requests

proxies = {
    "http":"170.39.118.187:3128",
    "https":"170.39.118.187:3128"
}

response = requests.get("http://httpbin/get", proxies=proxies)
print(response.text)