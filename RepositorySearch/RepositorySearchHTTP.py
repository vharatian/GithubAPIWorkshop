import json

import requests

params = {
    "q": "language:Java",
    "sort": "stars",
    "order": "desc"
}

response = requests.get("https://api.github.com/search/repositories", params = params)

with open(f"../results/repositories-http.json", 'w') as f:
    f.write(response.text)
