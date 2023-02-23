def chunkify_search_results(results):
    chunk_size = results.totalCount // 10  # get chunk_size for 10 workers
    if chunk_size == 0:
        chunk_size = 1
    for i in range(0, results.totalCount, chunk_size):
        yield results[i:i + chunk_size]
