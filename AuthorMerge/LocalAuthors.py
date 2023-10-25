import json

from pydriller import Repository

local_repo = Repository("../repositories/core")
local_info = {}
for commit in local_repo.traverse_commits():
    local_info[commit.hash] = ((commit.author.name, commit.author.email), (commit.committer.name, commit.committer.email))

with open(f"../results/local-auth.json", 'w') as f:
    f.write(json.dumps(local_info))
