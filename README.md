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

### Installing


You can clone the repository to your local directory 
```
git clone git@github.com:lixiaonin/workflow.git
```

Enter the project directory and start python console
```
cd workflow
python
```
then import workflow manager
```
from bin import *

WorkflowManager.run_workflow(full_path_of_workflow_file)
```

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
