import sys
import os
import logging
import urllib

class WorkflowParser(object):
    """ 
    Parse workflow file to data attributes. 
    """
    url = ''
    num_of_attempts = 3
    attempt_interval = 1
    file_path = ''

    def __init__(self, wf_path):
        self.wf_path = wf_path
        self._parse(wf_path)

    def _parse(self, wf_path):
        """ 
        Parse workflow file
        """
        for line in open(wf_path, 'r'):
            k, v = WorkflowParser._parse_line(line)
            if k == 'URL': 
                self.url = v
                if not self.url:
                    raise Exception('Invalid source URL.')
            elif k == 'NUM_OF_ATTEMPTS':
                if v:
                    self.num_of_attempts = int(v)
            elif k == 'ATTEMPT_INTERVAL':
                if v:
                    self.attempt_interval = int(v)
            elif k == 'FILE_PATH':
                if v and v[0] == '/':  
                    # absolute path
                    self.file_path = v
                else:  
                    # relative path to code
                    dir_path = os.path.dirname(os.path.realpath(__file__))
                    self.file_path = os.path.join(dir_path, v)
        if not self.url:
            raise Exception('Source URL missing.')

    @staticmethod
    def _parse_line(line):
        """ 
        Parse one line of settings to a (key, value) pair 
        """
        line = line[:line.find('#')] 
        j = line.find('=')
        k, v = line[:j], line[j+1:].rstrip('\n')
        return k.strip(), v.strip()

    def _print(self):
        """ internal print function for debuging """
        print '[Workflow - %s]' % self.wf_path
        print '  url                :',self.url
        print '  num_of_attempts    :',self.num_of_attempts
        print '  attempt_interval   :',self.attempt_interval
        print '  file_path          :',self.file_path


if __name__ == "__main__":
    mywf = WorkflowParser('inventory.workflow')
    mywf._print()

