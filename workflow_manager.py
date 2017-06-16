import os
from time import time
from workflow_parser import WorkflowParser
from data_parser import DataParser
from data_fetcher import DataFetcher
from helper import size_readable
from datetime import datetime


class WorkflowManager(object):

    def __init__(self):
        pass

    @staticmethod
    def run_workflow(wf_path):

        try:
            wf = WorkflowParser(wf_path)
            print '[Done]   [Workflow Parsing]'
        except Exception, e:
            print '[Failed] [Workflow Parsing] %s' % str(e)
            return

        try:
            start_time = time()
            df = DataFetcher(url=wf.url, attempt_count=wf.num_of_attempts, path=wf.file_path)
            print '[Done]   [Data Fetching] - %s seconds' % round(time() - start_time, 3)
        except Exception, e:
            print '[Failed] [Data Fetching] %s' % str(e)
            return

        try:
            start_time = time()
            dp = DataParser(url=wf.url, src_path=df.file_path)
            dp.read_n_process()
            print '[Done]   [Data Processing] - %s seconds' % round(time() - start_time, 3)
        except Exception, e:
            print '[Failed] [Data Processing] %s' % str(e)
            return

        try:
            start_time = time()
            size_stats = dp.write_stats()
            size_data = dp.write_data()
            dp.remove_raw()
            print '[Done]   [Data Writing] - %s seconds' % round(time() - start_time, 3)
        except Exception, e:
            print '[Failed] [Data Writing] %s' % str(e)
            return

        print '----------------------'
        print 'Output data  : %s' % size_readable(size_data)
        print 'Output stats : %s' % size_readable(size_stats)
        print '----------------------'
        print '[Success]'
        print '----------------------'


if __name__ == "__main__":
    # WorkflowManager.run_workflow('inventory.workflow')
    # WorkflowManager.run_workflow('inventory_bad_line.workflow')
    WorkflowManager.run_workflow('inventory_invalid_path.workflow')
