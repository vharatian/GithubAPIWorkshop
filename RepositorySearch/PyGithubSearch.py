from github import Github

from RepositorySearch.utils import write_json_file


def get_repository_with_language():
    """
       Sends a GET request to the GitHub API to retrieve repositories written in Java, sorted by stars in descending order.

       Parameters
       ----------
       None

       Returns
       -------
       list
           A list of dictionaries where each dictionary represents a repository and contains information about the repository's name and languages used.

       Notes
       -----
       The function uses the PyGithub library to search for repositories. It initializes a Github instance and uses the search_repositories method to retrieve repositories written in Java, sorted by stars in descending order. It retrieves the first 20 repositories from the search results. For each repository, it gets the languages used in the repository and adds a dictionary with the repository's name and languages to a list. The function then returns this list of repositories.
    """
    g = Github()
    results = []
    fetched_repositories = g.search_repositories(query="language:Java", sort='stars', order='desc')
    for i in range(20):
        repo = fetched_repositories[i]
        languages = repo.get_languages()
        results += [{"name": repo.name, "lang": languages}]

    return results


if __name__ == "__main__":
    results = get_repository_with_language()
    write_json_file("pygithub-search-lang.json", results)
