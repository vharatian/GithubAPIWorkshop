import json

import requests

page_size = 100

params = {
    "q": "Java",
    "per_page": 100,
    "sort": "stars",
    "order": "desc"
}

results = []
for i in range(10):
    params["page"] = i
    response = requests.get("https://api.github.com/search/repositories", params=params)
    response_json = json.loads(response.text)
    results += response_json['items']

    print(f"page: {i}")


with open(f"../results/repositories-http-page.json", 'w') as f:
    f.write(json.dumps(results))

