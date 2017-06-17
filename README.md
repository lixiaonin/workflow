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
git clone git@github.com:lixiaonin/workflow.git
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
![]({{site.baseurl}}/https://raw.githubusercontent.com/lixiaonin/workflow/master/Screen%20Shot%202017-06-16%20at%208.46.03%20PM.png)

If error happens, a message should be printed with erro details and the current step being attempted.
![]({{site.baseurl}}/https://raw.githubusercontent.com/lixiaonin/workflow/master/Screen%20Shot%202017-06-16%20at%208.49.00%20PM.png)

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```

	[Done]   [Workflow Parsing]
    [Done]   [Data Fetching] - 0.072 seconds
    [Done]   [Data Processing] - 0.001 seconds
    [Done]   [Data Writing] - 0.002 seconds
    Output data  : 7.3KB
    Output stats : 138.0B
    [Success]
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
