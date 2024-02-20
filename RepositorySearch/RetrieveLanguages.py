import json

import requests

from RepositorySearch.utils import write_json_file


def get_repository_with_language():
    """
        Retrieves repositories with a specific language from GitHub.

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list of dictionaries where each dictionary contains the name of the repository and its languages.

        Notes
        -----
        The function currently searches for repositories written in Java, sorted by stars in descending order,
        and retrieves a maximum of 10 repositories. The parameters for the search query can be modified within the function.
    """

    params = {
        "q": "Java",
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }

    response = requests.get("https://api.github.com/search/repositories", params=params)
    response_json = json.loads(response.text)

    results = []
    for repo in response_json["items"]:
        lang_res = requests.get(repo["languages_url"])
        lang_res_json = json.loads(lang_res.text)

        results += [{"name": repo["name"], "lang": lang_res_json}]


if __name__ == "__main__":
    results = get_repository_with_language()
    write_json_file("repositories-http-lang.json", results)
