# CS 456 GitHub API Workshop

This is a workshop for students to learn how to use GitHub API and more specific learn the following concepts.
1. HTTP API -> [Searching repositories](RepositorySearch/RepositorySearchHTTP.py) 
2. Pagination Logic -> [Fetching more repositories](RepositorySearch/RepositorySearchHTTPPage.py)
3. Repositories Details -> [Fetching language specific information](RepositorySearch/RetrieveLanguages.py)
4. GraphQL -> [Searching repositories and fetch details at once](RepositorySearch/RepositoryWithLanguage.py)
5. GitHUb API Wrappers -> [Searching repositories using PyGithub](RepositorySearch/PyGithubSearch.py) 
6. Parsing Commits -> [Merging authors using local and remote information](AuthorMerge)

## Setting up

### Clone the repository.

```bash
    git clone https://github.com/vharatian/GithubAPIWorkshop.git
    cd GithubAPIWorkshop
```

### Creating Virtual Environment and Install Requirements

```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

### Configuration (Required by task 4 and 6)
Copy the config-template.py file to the config.py file.

```bash
    cp config-template.py config.py
```

Obtain a valid github token and place it into the config.py file.
Look at the [GitHub Documentation](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) for more information.

### Evaluation Repository (Required by task 6)
To complete the GithubLogin task you need to clone the VueJS core repository into the `repositories` folder.

```bash
    mkdir repositories
    git clone https://github.com/vuejs/core.git repositories/core
```

## Results

The results of each task should be placed as a JSON file in a folder named `results` in the directory you have launched the execution.
