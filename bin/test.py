import os
from workflow_manager import WorkflowManager

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
