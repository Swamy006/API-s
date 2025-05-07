import requests
import json

url="https://jsonplaceholder.typicode.com/posts/1"

data={"id":"1",
    "book_title":"Amma diary lo konni pagelu",
"poet":"Ravi_mantri",
"poet_id":"1"}

response=requests.put(url,data=data)
if response.status_code==200:
    print(json.dumps(response.json(), indent=4))
else:
    print("ERROR:",response.status_code)



