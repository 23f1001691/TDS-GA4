import requests

url = "http://127.0.0.1:8000/similarity"

payload = {
    "docs": ["Doc 1 text", "Doc 2 text", "Doc 3 text"],
    "query": "Find info about project X"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

