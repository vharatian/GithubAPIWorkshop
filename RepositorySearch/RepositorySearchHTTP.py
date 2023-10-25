import json

import requests
import os


params = {
    "q": "language:Java",
    "sort": "stars",
    "order": "desc"
}

response = requests.get("https://api.github.com/search/repositories", params = params)

folder_path = "../results/"
if not os.path.exists(folder_path):
   os.makedirs(folder_path)

with open(f"../results/repositories-http.json", 'w', enconding="utf-8") as f:
    f.write(response.text)

