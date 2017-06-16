import os 
import re
import sys
import json
from median import Median
from helper import size_readable


class DataParser(object):
    """ 
    Parse locally saved .tsv file to JSON file 
    """
    
    def __init__(self, src_path='', url=''):
        self.url = url
        # path
        self.src_path = src_path
        self.des_path_data = self.src_path.replace('.tsv', '_data.json')
        self.des_path_stats = self.src_path.replace('.tsv', '_stats.json')
        # data
        self.data = []
        self.min_15 = sys.maxint
        self.max_15 = 0
        self.med_15 = None
        self.running_median = Median()

    @staticmethod
    def _cleaned_volume(v):
        """ 
        Clean volume data, return -1 if invalid data 
        rtype: float
        """
        try:
            v = v.strip('-').rstrip('\n')
            return float(v)
        except:
            return -1.0

    @staticmethod
    def _cleaned_rank(r):
        """ 
        Clean rank data, return -1 if invalid
        rtype: int 
        """
        try:
            r = r.strip('*')
            return int(r)
        except:
            return -1

        
    def read_n_process(self):
        """ 
        Read data from raw file,
        convert to organized data,
        and calculate min, max and median in parallel
        """
        f = open(self.src_path, 'r')
        for i, line in enumerate(f):
            try:
                # skip header row.
                if i == 0: continue
                # assign columns in a row to variables.
                rank, port_str, v15, v14, v13, v12, v11 = [col for col in line.split('\t')]
                # split port and country.
                comma = port_str.find(',')
                port, country = port_str[:comma].strip(), port_str[comma+1:].strip()
                # record min, max, median of yer 2015(column 3).
                v15 = DataParser._cleaned_volume(v15)
                if v15 != -1:
                    self.min_15 = min(self.min_15, v15)
                    self.max_15 = max(self.max_15, v15)
                    self.running_median.add_num(v15)
                    self.med_15 = self.running_median.get_median()
                # add parsed row to cache.
                self.data.append({
                    '_id': i,
                    'rank': DataParser._cleaned_rank(rank),
                    'port': port,
                    'country': country,
                    'volume': {
                        'v15': v15,
                        'v14': DataParser._cleaned_volume(v14),
                        'v13': DataParser._cleaned_volume(v13),
                        'v12': DataParser._cleaned_volume(v12),
                        'v11': DataParser._cleaned_volume(v11)
                        },
                    })
            except Exception, e:
                print '    [Warning][Data Parsing] uncleanable data: %s' % repr(line)
        f.close()

    def remove_raw(self):
        """ 
        Delete raw data. 
        """
        os.remove(self.src_path)

    def write_data(self):
        """ 
        Write whole data file to JSON 
        """
        try:
            with open(self.des_path_data, 'w') as f:
                json.dump({
                    'data': self.data,
                    'meta': {
                        'src': self.url,
                        },
                    }, f)
            f.close()
            return os.path.getsize(self.des_path_data)
        except Exception, e:
            raise Exception('write whole file err : %s' % str(e))

    def write_stats(self):
        """ 
        Write statistical data to JSON 
        """
        try:
            with open(self.des_path_stats, 'w') as f:
                json.dump({
                    'min': self.min_15,
                    'max': self.max_15,
                    'median': self.med_15,
                    'meta': {
                        'src': self.url,
                        },
                    }, f)
            f.close()
            return os.path.getsize(self.des_path_stats)
        except Exception, e:
            raise Exception('write stats file err : %s' % str(e))


if __name__ == "__main__":
    from workflow_parser import WorkflowParser
    from data_fetcher import DataFetcher
    from pprint import pprint

    dir_path = os.path.dirname(os.path.realpath(__file__))

    wfp = WorkflowParser('dataset002')
    df = DataFetcher(
            url=wfp.url, 
            attempt_count=wfp.num_of_attempts,
            path=wfp.file_path,
            )
    df.fetch()

    dp = DataParser(
            url=wfp.url,
            src_path=df.file_path, 
            )
    dp.read_n_process()
    size_stats = dp.write_stats()
    size_data = dp.write_data()
    print 'Output data  : %s' % size_readable(size_data)
    print 'Output stats : %s' % size_readable(size_stats)
    print '[Sucess] '
