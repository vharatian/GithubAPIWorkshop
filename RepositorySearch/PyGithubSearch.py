import json

from config import TOKEN
from github import Github

# g = Github(login_or_token=TOKEN)
g = Github()
results = []
fetched_repositories = g.search_repositories(query="language:Java", sort='stars', order='desc')
for i in range(20):
    repo = fetched_repositories[i]
    languages = repo.get_languages()
    results += [{"name": repo.name, "lang": languages}]

with open(f"../results/pygithub-search-lang.json", 'w') as f:
    f.write(json.dumps(results))
