import json
import requests
from RepositorySearch.utils import write_json_file


def get_repositories():
    """
        Retrieves repositories written in Java from GitHub, sorted by stars in descending order.

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list of dictionaries where each dictionary represents a repository and contains information about the repository.

        Notes
        -----
        The function sends 10 GET request to the GitHub API to retrieve repositories. It retrieves a maximum of 10 repositories per page and retrieves a total of 10 pages. The parameters for the search query can be modified within the function.
    """

    params = {
        "q": "Java",
        "per_page": 10,
        "sort": "stars",
        "order": "desc"
    }

    repos = []
    for i in range(10):
        params["page"] = i
        response = requests.get("https://api.github.com/search/repositories", params=params)
        response_json = json.loads(response.text)
        repos += response_json['items']

        print(f"page: {i}")

    return repos


if __name__ == "__main__":
    repos = get_repositories()
    write_json_file("repositories-http-page.json", repos)
