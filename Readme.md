# Readme for this house_postdoc repository
### AUTOGENERATED BY SWE for Science kickstart generator - www.sweforscience.com - www.twitter.com/sweforscience 
### Package Author: rikiya@stanford.edu and Binglan Li

This project draws a house using python standard library "turtle". See [the design document](Design.md) for more info.

## How to set up the python environment

There are two ways to set up the python environment.

1. Using pyenv/venv (Binglan)

1. Using conda (Rikiya)
- Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html#linux-installers) on your machine (download the distribution that comes with python3).  
- Create a conda environment:
```
conda create -n my_turtle python=3.8
```  
- Activate the environment:
```
conda activate my_turtle
```  

## Demo
### Run with default configuration
```
python py/house_postdoc_cli.py
```
- default values are: `--window 4 --garage 2 --door 1 --tree 2 --cloud 1`

### You can change the numbers of windows, garage doors, doors, trees, and clouds by specifying the arguments
```
python py/house_postdoc_cli.py --window 8 --garage 3 --door 2 --tree 3 --cloud 2 
```
or
```
python py/house_postdoc_cli.py -w 8 -g 3 -d 2 -t 3 -c 2 
```

## Code structure:
```.
├── Dockerfile
├── Makefile
├── Readme.md
├── Design.md
└── py
    ├── house_postdoc_cli.py
    ├── house_postdoc_jupyter.ipydb
    ├── house_postdoc_lib.py
    ├── house_postdoc_unittest.py
    ├── house_postdoc_webserver.py
    ├── package-lock.json
    ├── package.json
    ├── requirements.txt
    ├── serverless.yml
    └── templates
        └── form.html 
```
  
  
  
  
  
  
  
  
  
## How to modify this autogenerated repository for your project:

This repository has been automatically generated for you by [SWE for Science](www.sweforscience.com).  In order to make use of it, you will need to customize the scripts. Here's a rough guide for your use:

1. Run `make setup` and then run `make test`.  Ensure that the unittests run correctly.
1. Enter the virtual environment by running `source venv/bin/activate`
1. Set up a github repository, then push this repository to the github repo by following the instructions on the site, then run `git push`
1. Edit the [design document template](Design.md): `Design.md`
1. Periodically commit to git using `git add`, `git commit`, `git push`, as required.
1. Modify house_postdoc_lib.py and add your logic/code
1. Modify house_postdoc_unittest.py to add some tests for your code
1. Continue the above two steps until `make test` passes.
1. Modify house_postdoc_cli.py to make a command-line interface for your code.
<!-- 1. Modify (or delete) house_postdoc_webserver.py -->
<!-- 1. You may add additional python dependencies using pip install *but ensure that your venv is activated before doing so, and ensure that you run `make venv-freeze` before committing and pushing code* -->
<!-- 1. If you are using a webserver, you may deploy code to *AWS Lambda* by running `sls deploy` from the `py/` directory.  You may need to edit the `serverless.yml` file. Before doing this, you will need to go to the [AWS IAM console](https://console.aws.amazon.com/iam/home#/users$new?step=details) and  grant the following permissions to the AWS IAM account which you're using here: 
```IAMFullAccess
  AmazonS3FullAccess
  AmazonAPIGatewayInvokeFullAccess
  CloudWatchFullAccess
  AmazonAPIGatewayAdministrator
  AWSCloudFormationFullAccess
  AWSLambda_FullAccess 
  ``` -->


 *_NOTE: Delete this  section once you've figured this out._*


## Setup

NB: The prerequisites for this repository are python3, nodejs, and npm. Ensure you have installed these (either using brew if you're on MacOS, or apt-get if you are on *NIX).

In order to set up the environment, run `make setup`. This will set up a virtual environment and download all dependencies.


## Code structure:
```.
├── Dockerfile
├── Makefile
├── Readme.md
├── Design.md
└── py
    ├── house_postdoc_cli.py
    ├── house_postdoc_jupyter.ipydb
    ├── house_postdoc_lib.py
    ├── house_postdoc_unittest.py
    ├── house_postdoc_webserver.py
    ├── package-lock.json
    ├── package.json
    ├── requirements.txt
    ├── serverless.yml
    └── templates
        └── form.html 
```

The Makefile in contains a number of useful targets. Run `make help` to see how to use it. `make TARGET` is how you invoke a particular target.

*house_postdoc_cli.py* This is the command-line interface for this program. _TODO: REPLACE THIS DESCRIPTION_

*house_postdoc_webserver.py* This is the Flask-based web server for this program. _TODO: REPLACE THIS DESCRIPTION_

*house_postdoc_unittest.py* This has unittests for this program. These can be run with `make test`.  _TODO: REPLACE THIS DESCRIPTION_

*package.json/package-lock.json* These files are for the NPM dependencies used by serverless/AWS lambda deploy scripts.

*requirements.txt* This contains pip dependencies for this project. Use `make venv-freeze` to update.

*serverless.yml* Contains configuration for AWS lambda deployment of the webserver.

*templates* Contains HTML templates for the webserver.

