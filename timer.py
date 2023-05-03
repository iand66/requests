import requests

#response = requests.get("https://httpbin.org/delay/3")
#print(response.json())

for _ in [1,2,3]:
    try:
        response = requests.get("https://httpbin.org/delay/5", timeout=5)
        print(response.json())
    except:
        continue
    