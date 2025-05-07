import requests
import json
url = "https://jsonplaceholder.typicode.com/posts/1"  # Replace '1' with the ID of the poet or resource to delete

# Make the DELETE request
response = requests.delete(url)

# Check the response status
if response.status_code == 200:
    print("Resource deleted successfully!")
else:
    print("Error:", response.status_code)