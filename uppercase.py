import requests

url = "https://hal9.com/annarg/uppercase/"
# url = "http://localhost:8000/"
API_KEY = "H9PGRCGFSYMYVYMOQSAQHWHDNQHVOIKYPG"

input_data = { "text": "hello" }

response = requests.post(
    url,
    headers={"Authorization": f"Bearer {API_KEY}"},
    json=input_data
)

print(response.status_code)
print(response.text)
