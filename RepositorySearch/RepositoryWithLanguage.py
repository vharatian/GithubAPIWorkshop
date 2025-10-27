import json

from config import TOKEN
import requests

from RepositorySearch.utils import write_json_file


def get_repository_with_language():
    """
        Sends a POST request to the GitHub GraphQL API to retrieve repositories.

        Parameters
        ----------
        None

        Returns
        -------
        requests.models.Response
            The response from the GitHub GraphQL API.

        Notes
        -----
        The function reads a GraphQL query from the file 'repoSearchQuery.graphql' and uses it in the POST request.
        The 'Authorization' header is set using a token from the 'config' module.
    """

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    with open(f"./repoSearchQuery.graphql") as f:
        query = f.read()

    return requests.post("https://api.github.com/graphql", headers=headers, json={"query": query})


if __name__ == "__main__":
    response = get_repository_with_language()
    data = json.loads(response.text)
    write_json_file("repositories-graphql-lang.json", data)
