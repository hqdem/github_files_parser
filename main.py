from githib_api.github_client import GithubClient

from githib_api.utils import chunkify_search_results


def main():
    github_client = GithubClient()
    search_results = github_client.search_repos_by_language(lang='verilog')


if __name__ == '__main__':
    main()
