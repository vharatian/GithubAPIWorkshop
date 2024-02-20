import json
import traceback

import requests
from pydriller import Repository

from config import TOKEN

from RepositorySearch.utils import write_json_file


class UserInfo:
    @staticmethod
    def from_github_actor(actor):
        if actor is None:
            return None

        login = None
        if actor["user"] is not None:
            login = actor["user"]["login"]

        return UserInfo(actor["name"], actor["email"], login)

    def __init__(self, name, email, login=None):
        self.name = name
        self.email = email
        self.login = login


def read_github_repository(github_token, repository_owner, repository_name):
    """
        Reads the GitHub repository and returns a dictionary with commit information.

        Parameters
        ----------
        github_token : str
            The GitHub token used for authentication.
        repository_owner : str
            The owner of the repository.
        repository_name : str
            The name of the repository.

        Returns
        -------
        dict
            A dictionary where the keys are commit OIDs and the values are tuples containing the author and committer
            as UserInfo objects.

        Raises
        ------
        Exception
            If there is an error in the request or processing the response.
        """

    github_info = {}
    try:
        headers = {
            "Authorization": f"Bearer {github_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }

        with open(f"./commitQueryTemplate.graphql") as f:
            query_template = f.read()

        query_template = query_template.replace("owner-placeholder", repository_owner)
        query_template = query_template.replace("name-placeholder", repository_name)

        cursor = None
        while True:
            if cursor is None:
                query = query_template.replace('after:"template"', '')
            else:
                query = query_template.replace('after:"template"', f'after:"{cursor}"')

            response = requests.post("https://api.github.com/graphql", headers=headers, json={"query": query})
            # log(response.text)
            response_json = json.loads(response.text)
            commits = response_json["data"]["repository"]["defaultBranchRef"]["target"]["history"]["edges"]
            if len(commits) == 0:
                break

            for commit in commits:
                commit_data = commit["node"]
                author = UserInfo.from_github_actor(commit_data["author"])
                committer = UserInfo.from_github_actor(commit_data["committer"])
                github_info[commit_data["oid"]] = (author, committer)

            cursor = commits[-1]["cursor"]
            print(f"Next request cursor {cursor}")

    except Exception as e:
        print(e)
        print(traceback.format_exc())

    return github_info


def get_local_info(local_path):
    """
        Retrieves commit information from a local repository.

        Parameters
        ----------
        local_path : str
            The path to the local repository.

        Returns
        -------
        dict
            A dictionary where the keys are commit hashes and the values are tuples containing the author and committer.
        """
    local_repo = Repository(local_path)
    local_info = {}
    for commit in local_repo.traverse_commits():
        local_info[commit.hash] = (commit.author, commit.committer)

    return local_info


def check_if_github_has_more_data(local, github):
    if github[0] is not None and github[1] is not None:
        return True

    if github[0] is None and github[1] is not None and local[1] != github[1]:
        return True

    if github[1] is None and github[0] is not None and local[0] != github[0]:
        return True

    return False


def merge_users_info(local, github):
    users = []
    if github:
        local = (local.name, local.email, github.login)
        users += [local]
        github = (github.name, github.email, github.login)
        if check_if_github_has_more_data(local, github):
            users += [github]
    else:
        users += [(local.name, local.email, None)]

    return users


def create_users_data(local_info, github_info):
    users_data = []
    for c in local_info:
        if c in github_info:
            local_author = local_info[c][0]
            local_committer = local_info[c][1]
            github_author = github_info[c][0]
            github_committer = github_info[c][1]

            users_data += merge_users_info(local_author, github_author)
            users_data += merge_users_info(local_committer, github_committer)
        else:
            local_author = local_info[c][0]
            local_committer = local_info[c][1]
            users_data += [(local_author.name, local_author.email, None)]
            users_data += [(local_committer.name, local_committer.email, None)]

    return users_data


def merge_based_on_login(user_data):
    results = {}
    for u in user_data:
        login = u[2]
        if login is not None:
            if login in results:
                results[login]["name"].add(u[0])
                results[login]["email"].add(u[1])
            else:
                results[login] = {"name": set([u[0]]), "email": set([u[1]])}

    return results


if __name__ == "__main__":
    localInfo = get_local_info("../repositories/core")
    github_info = read_github_repository(TOKEN, "vuejs", "core")
    user_data = create_users_data(localInfo, github_info)
    merge_result = merge_based_on_login(user_data)

    final_result = {}
    for login in merge_result:
        if len(merge_result[login]["name"]) > 1 or len(merge_result[login]["email"]) > 1:
            final_result[login] = {"name": list(merge_result[login]["name"]), "email": list(merge_result[login]["email"])}

    write_json_file("merge-github.json", final_result)

    print("end")
