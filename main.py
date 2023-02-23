from githib_api.github_client import GithubClient

from githib_api.utils import chunkify_search_results
from utils import get_date_intervals
from db.repositories.created_intervals import CreatedIntervalsRepository
from db.session import session
from db.init_db import init_db


def main():
    github_client = GithubClient()

    search_results = github_client.search_repos_by_language(lang='verilog')
    result_chunks = chunkify_search_results(search_results, 100)
    intervals = get_date_intervals()

    init_db()

    db_repo = CreatedIntervalsRepository(session)
    db_repo.fill_db_with_intervals(intervals)


if __name__ == '__main__':
    main()
