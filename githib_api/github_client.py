from github import Github

from config import Config


class GithubClient:
    def __init__(self):
        self._client = Github(login_or_token=Config.github_access_token)

    def search_repos_by_language(self, lang):
        return self._client.search_repositories(query=f'language:{lang}')
