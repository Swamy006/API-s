import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)
if response.status_code==200:
    print(json.dumps(response.json(), indent=4))
else:
    print("Error:",response.status_code)
