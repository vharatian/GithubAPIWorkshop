import json

import requests

from RepositorySearch.utils import write_json_file


def get_repositories():
    """
        Sends a GET request to the GitHub API to retrieve repositories written in Java, sorted by stars in descending order.

        Parameters
        ----------
        None

        Returns
        -------
        requests.models.Response
            The response from the GitHub API, which includes the repositories that match the search criteria.

        Notes
        -----
        The function sets up the parameters for the request to search for repositories written in Java, sort the repositories by the number of stars, and order the sorted repositories in descending order. The function then sends the GET request with these parameters and returns the response from the GitHub API.
    """
    params = {
        "q": "language:Java",
        "sort": "stars",
        "order": "desc"
    }

    return requests.get("https://api.github.com/search/repositories", params=params)


if __name__ == "__main__":
    response = get_repositories()
    data = json.loads(response.text)
    write_json_file("repositories-http.json", data)
