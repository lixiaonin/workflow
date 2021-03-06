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
            print '    [Done]   [Workflow Parsing]'
        except Exception, e:
            print '    [Failed] [Workflow Parsing] %s' % str(e)
            return

        try:
            start_time = time()
            df = DataFetcher(url=wf.url, attempt_count=wf.num_of_attempts, path=wf.file_path)
            print '    [Done]   [Data Fetching] - %s seconds' % round(time() - start_time, 3)
        except Exception, e:
            print '    [Failed] [Data Fetching] %s' % str(e)
            return

        try:
            start_time = time()
            dp = DataParser(url=wf.url, src_path=df.file_path)
            dp.read_n_process()
            print '    [Done]   [Data Processing] - %s seconds' % round(time() - start_time, 3)
        except Exception, e:
            print '    [Failed] [Data Processing] %s' % str(e)
            return

        try:
            start_time = time()
            size_stats = dp.write_stats()
            size_data = dp.write_data()
            dp.remove_raw()
            print '    [Done]   [Data Writing] - %s seconds' % round(time() - start_time, 3)
        except Exception, e:
            print '    [Failed] [Data Writing] %s' % str(e)
            return

        print '    Output data  : %s' % size_readable(size_data)
        print '    Output stats : %s' % size_readable(size_stats)
        print '    [Success]'


if __name__ == "__main__":
    
    pwd = os.path.dirname(os.path.realpath(__file__))
    def test_wf_manager(path):
        file_path = os.path.join(pwd, path)
        print 'Workflow manager test : %s -----' % path
        WorkflowManager.run_workflow(file_path)
        print
        print

    test_wf_manager('../inventory_invalid_path.workflow')
    test_wf_manager('../inventory_bad_line.workflow')
    test_wf_manager('../inventory.workflow')
