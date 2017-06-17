import os
from workflow_manager import WorkflowManager

pwd = os.path.dirname(os.path.realpath(__file__))


def test_wf_manager(title, path):
    ''' 
    Helper function to run test and print info to console
    '''
    file_path = os.path.join(pwd, path)
    print '*%s* test : %s -----' % (title, path)
    WorkflowManager.run_workflow(file_path)
    print
    print

test_wf_manager('Normal', '../inventory.workflow')
test_wf_manager('Bad source url', '../inventory_bad_url.workflow')
test_wf_manager('Invalid output path', '../inventory_invalid_path.workflow')
test_wf_manager('Bad line of data in tsv file', '../inventory_bad_line.workflow')
test_wf_manager('Normal with larger tsv', '../dataset002.workflow')
