import os
from github import Github

from config import Config


class GithubClient:
    def __init__(self):
        self._client = Github(login_or_token=Config.github_access_token)

    def search_repos_by_language(self, lang, start_time=None, end_time=None):
        if start_time is None and end_time is None:
            return self._client.search_repositories(query=f'language:{lang}')
        return self._client.search_repositories(query=f'language:{lang}+created:{start_time}..{end_time}')

    def download_files_by_ext(self, repos, ext, save_path):
        for repo in repos:
            repo_name = repo.full_name.replace('/', '__')
            if not os.path.exists(f'{save_path}/{repo_name}'):
                os.mkdir(f'{save_path}/{repo_name}')
            else:
                continue
            contents = repo.get_contents("")
            while contents:
                file_content = contents.pop(0)
                if file_content.type == "dir":
                    contents.extend(repo.get_contents(file_content.path))
                else:
                    print(f'Processing {file_content}')
                    if file_content.name.endswith(ext):
                        with open(f'{save_path}/{repo_name}/{file_content.name}', 'wb') as f:
                            try:
                                f.write(file_content.decoded_content)
                            except AssertionError:
                                print(f'Unable to write {file_content.name}. No encoding specified.')
