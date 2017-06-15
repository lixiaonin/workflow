import os
import time
from requests import get as get_url
from requests.exceptions import *

dir_path = os.path.dirname(os.path.realpath(__file__))

class DataFetcher(object):

    def __init__(self, url, attempt_count=3, attempt_interval=1, path=''):
        # fetcher settings.
        self.url = url
        self.file_path = os.path.join(path, url.split('/')[-1])
        self.attempt_count = attempt_count
        self.attempt_interval = attempt_interval
        # mkdir for data directory if not exist.
        if not os.path.exists(path):
            os.makedirs(path)
        # fetch data.
        self.fetch()

    def fetch(self):
        for i in xrange(self.attempt_count):
            try:
                response = get_url(self.url, stream=True)
                with open(self.file_path, 'wb') as out_file:
                    for chunk in response.iter_content(chunk_size=1024): 
                        if chunk:
                            out_file.write(chunk)
                del response
                return self.file_path
            except (ConnectionError, Timeout):
                print '[Retry] Connerction error'
                self.attempt_count -= 1
                if not self.attempt_count:
                    raise Exception('Maximum number of attempts reached') 
                time.sleep(self.attempt_interval)

    def _print(self):
        print 'url',self.url
        print 'file_path',self.file_path
        print 'attempt_count',self.attempt_count
        print 'attempt_interval',self.attempt_interval


if __name__ == "__main__":
    from workflow_parser import WorkflowParser
    wfp = WorkflowParser('inventory.workflow')
    df = DataFetcher(
            url=wfp.url,
            attempt_count=wfp.num_of_attempts,
            path=wfp.file_path,
            )
