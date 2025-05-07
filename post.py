import requests
import json

url="https://jsonplaceholder.typicode.com/posts"

data={"book_id":"1",
    "book_title":"Amma diary lo konni pagelu",
"poet":"Amma"}
response=requests.post(url,data=data)
if response.status_code==201:
    print(json.dumps(response.json(), indent=4))
else:
    print("Error:",response.status_code)