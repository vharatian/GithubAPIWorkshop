import json

import requests

params = {
    "per_page": 100,
    "page": 0,
}

response = requests.get("https://api.github.com/repos/vuejs/core/commits", params=params)

with open(f"../results/github-commit-api-http.json", 'w') as f:
    f.write(response.text)