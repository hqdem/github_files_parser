from threading import Thread


class DownloadFilesWorker(Thread):
    def __init__(self, queue, github_client):
        super().__init__()
        self._queue = queue
        self._github_client = github_client

    def run(self):
        while True:
            repos, ext, save_path = self._queue.get()
            try:
                self._github_client.download_files_by_ext(repos, ext=ext, save_path=save_path)
            finally:
                self._queue.task_done()
