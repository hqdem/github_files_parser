def chunkify_search_results(results, size):
    for i in range(0, results.totalCount, size):
        yield results[i:i + size]
