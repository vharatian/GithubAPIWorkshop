import requests

from tqdm import tqdm

from config import TOKEN

# Replace 'your_github_token' with your actual GitHub token
GITHUB_TOKEN = TOKEN
GITHUB_API_URL = "https://api.github.com/graphql"


# Define GraphQL query to fetch repositories with their languages, sorted by stars in descending order
def fetch_repositories(after_cursor=None):
    query = """
    query ($cursor: String) {
      search(query: "stars:>1000", type: REPOSITORY, first: 50, after: $cursor) {
        pageInfo {
          endCursor
          hasNextPage
        }
        edges {
          node {
            ... on Repository {
              name
              owner {
                login
              }
              stargazers {
                totalCount
              }
              languages(first: 10) {
                edges {
                  node {
                    name
                  }
                  size
                }
                totalSize
              }
            }
          }
        }
      }
    }
    """
    variables = {"cursor": after_cursor}
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

    response = requests.post(GITHUB_API_URL, json={"query": query, "variables": variables}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed to run: {response.status_code}, {response.text}")


# Function to calculate percentage of languages
def calculate_language_percentage(languages):
    total_size = languages['totalSize']
    language_percentages = {}
    for lang in languages['edges']:
        lang_name = lang['node']['name']
        lang_size = lang['size']
        percentage = (lang_size / total_size) * 100
        language_percentages[lang_name] = percentage
    return language_percentages


# Fetch repositories and filter for Java-dominant ones
def fetch_top_java_repositories():
    top_java_repos = []
    cursor = None
    total_repos = 100
    with tqdm(total=total_repos, desc="Fetching repositories") as pbar:
        while len(top_java_repos) < total_repos:
            result = fetch_repositories(after_cursor=cursor)
            repositories = result['data']['search']['edges']

            for repo in repositories:
                repo_node = repo['node']
                languages = repo_node['languages']
                language_percentages = calculate_language_percentage(languages)

                if 'JavaScript' in language_percentages and language_percentages['JavaScript'] > 95:
                    top_java_repos.append({
                        "name": repo_node['name'],
                        "owner": repo_node['owner']['login'],
                        "stars": repo_node['stargazers']['totalCount'],
                        "js_percentage": language_percentages['JavaScript']
                    })
                    pbar.update(1)
                    if len(top_java_repos) >= total_repos:
                        break

            cursor = result['data']['search']['pageInfo']['endCursor']
            if not result['data']['search']['pageInfo']['hasNextPage']:
                break

    return top_java_repos[:100]


# Main function to execute the process
if __name__ == "__main__":
    try:
        top_java_repositories = fetch_top_java_repositories()
        print(f"Found {len(top_java_repositories)} repositories with more than 95% Java code:")
        for repo in top_java_repositories:
            print(f"{repo['owner']}/{repo['name']} - {repo['js_percentage']:.2f}% Java, {repo['stars']} stars")
    except Exception as e:
        print(f"Error: {str(e)}")
