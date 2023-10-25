import json

import requests

params = {
    "q": "Java",
    "sort": "stars",
    "order": "desc",
    "per_page": 10
}

response = requests.get("https://api.github.com/search/repositories", params = params)
response_json = json.loads(response.text)

results = []
for repo in response_json["items"]:
    lang_res = requests.get(repo["languages_url"])
    lang_res_json = json.loads(lang_res.text)

    results += [{"name": repo["name"], "lang": lang_res_json}]

with open(f"../results/repositories-http-lang.json", 'w') as f:
    f.write(json.dumps(results))
