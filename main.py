from githib_api.github_client import GithubClient


def main():
    github_client = GithubClient()
    search_results = github_client.search_repos_by_language(lang='verilog')
    print(search_results.totalCount)


if __name__ == '__main__':
    main()
