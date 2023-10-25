from config import TOKEN
import requests

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

with open(f"./repoSearchQuery.graphql") as f:
    query = f.read()

response = requests.post("https://api.github.com/graphql", headers=headers, json={"query": query})

with open(f"../results/repositories-graphql-lang.json", 'w') as f:
    f.write(response.text)
