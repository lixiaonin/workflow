# Workflow Manager

A simple workflow manager that follows directions from a .workflow file to download .tsv file from web and parse the data and save cleaned data to JSON files.

## Getting Started

These instructions will get you a copy of the Workflow Manager up and running on your local machine.

### Prerequisites

You will need python2.7 to run this project.

For MacOS or OS X
```
brew install python
```

For Ubuntu
```
sudo apt-get install python
```

### Installing & How to Use


You can clone the repository to your local directory 
```
git clone https://github.com/lixiaonin/workflow.git
```

Then create a workflow file and open the file.
```
touch inventory.workflow
vim inventory.workflow
```

Add the following setting lines to the file (order doesn't matter).
```
# keywords should be on left side of '=' symbol and values are one right side.
# '#' is single line comment, all characters after '#' will not be catched by the program

# url of the source tsv file, required.
URL = https://raw.githubusercontent.com/lixiaonin/workflow/master/inventory.tsv

# number of URL call attempts before it fails. default is 3 if not provided
NUM_OF_ATTEMPTS = 3

# the interval between two URL call attempts(in second). default is 1 sec.
ATTEMPT_INTERVAL = 1

# output path for JSON files, can be either absolute or relative path. default is current directory.
FILE_PATH = data_directory

```

Save the workflow file and open python console.
Import WorkflowManager and call static method run_workflow directly.
```
from workflow import WorkflowManager

WorkflowManager.run_workflow('inventory.workflow')
```
If the entire workflow completes successfully, [Success] will be printed to the console at the end. 

![alt text](https://raw.githubusercontent.com/lixiaonin/workflow/master/Screen%20Shot%202017-06-16%20at%208.46.03%20PM.png)

If error happens, a message should be printed with error details and the current step being attempted.
![alt text](https://raw.githubusercontent.com/lixiaonin/workflow/master/Screen%20Shot%202017-06-16%20at%208.49.00%20PM.png)


## Break down the components


**workflow_manager.py** - core logic of workflow manager.

**workflow_parser.py** - parse workflow definition/setting file.

**data_fetcher.py** - fetch data from remote URL and save raw data locally(delete when workflow is successfully executed)

**data_parser.py** - read raw data, clean data, calculate running maximum, minimum and median values for the 2015 Volume column. And write both in JSON to disk files.

**helper.py** - small helper function such as convert byte number to human readable string.

**median.py** - a running median calculator that takes value stream and calculate current median in efficient manner.

**test.py** - script to run test cases

***dataset_generator.py** - a fake tsv file generator for test purposes.



## Running the tests

Test cases is put in /bin/test.py, to run the testcases you can simply:
```
python workflow/bin/test.py
```
And you should be able to see the results of a sequence of tests including:

1, Normal execution, inventory.tsv, Success

2, Bad source URL, Fail

3, Invalid output path in workflow definition file, Fail

4, Bad data line in tsv file, Warning, Success

Saved JSON files can be found in /data directory.

