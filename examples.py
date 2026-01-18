import requests

url = "http://127.0.0.1:5000/predict"

input_data = {
    "text": "A quick brown fox jumps over the lazy dog."
}

response = requests.post(url, json=input_data)
print(response.json())