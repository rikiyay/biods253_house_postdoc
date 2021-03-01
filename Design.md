# Design Document

## Overview

The very first mini-assignment of the course BIODS 253 (2021 winter) is to draw an image of house using a python (>=3) standard library "turtle graphics". Our team, the house of postdocs, is constituted of two members, Binglan Li and Rikiya Yamashita.

## Background: 

One month into the course BIODS253 of software engineering (SWE), it is time to practice the SWE knowledge that has been hitherto taught in class. 
### Motivations

To practice and understand SWE. This simple project can help establish a good SWE awareness and practice that can be extended and applied to our future projects.

### Other solutions

N/A

### Current Goals

1. We initialized this repo by using [SWE for Science](www.sweforscience.com).
2. Create a python program that receives users' input to draw an image of a nice looking house. 

**Phase I**

1. The image of house will have the following fixed numbers of components.
    - 4 windows
    - 2 garage doors
    - 1 door
    - 2 trees
    - 1 clouds

**Phase II**

1. An interactive feature: will allow users to specify different numbers of objects in the image of a house.
2. Establish proper unit tests

### Non-Goals

1. We won't draw a castle.
2. We won't host a web server from AWS.
3. We will not support choices of alternative colors.

### Future goals

1. Run a local web server using Docker to receive users' input.

## Detailed Design

We will draw the draft using draw.io. Draw.io creates an XML file that is currently hosted on Google Drive (https://drive.google.com/file/d/1oKM5badNSETzD_BiwFQ3YALojEdTDxf5/view?usp=sharing). 

We will develop a `Python-cli` that accepts integer numbers of windows, garage doors, house doors, trees, and clouds as arguments (Only allow integers for any arguments) from users. There will be a checkpoint that validates whether input arguments are integers. If not, the program returns an error and exit. If inputs are integers, the program will invoke functions in the `python_lib` to draw an image. 

We will develop a `python_lib` that defines a class of Turtle objects. This Turtle class will contain functions to create objects of a house using Turtle.


### User requirements

1. Need to have a python >= 3.5 environment (preferably 3.8)
2. In the interactive mode, users need to specify minimum and maximum numbers of objects.
    - 1 <= windows <= _ (set a default value = 4)
    - 1 <= garage doors <= _ (set a default value = 2)
    - 1 <= doors <= _ (set a default value = 1). You must have at least one door to get in or out of a house.
    - 1 <= trees <= _ (set a default value = 2)
    - 1 <= clouds <= _ (set a default value = 1)

### Data validation/what are potential error states?

- Non-integer arguments -> Return error.

### Logging/monitoring/observability

We will log program progress and error messages to an independent output log file.

### What will you test?

TBD (depending on what functions we will implement)

## Third Party dependencies

- Python (>= 3, tested on version 3.8.7)
- Needed for unit tests
    - numpy
    - Pillow
    - ghostscript

## Work Estimates

This project is due Feb 28 (Sun).

## Homework Logging

1. We have different ways of using python and python packages. 
- Binglan will use pyenv (and venv) for python = 3.8.7 (Binglan's default version)
- Rikiya will use conda for python=3.8.5 (conda only allowed me to install 3.8.5, so we have a little compatibility issue here -> docker may be a good solution but will try to see how the current setting works)

2. Question from Rikiya: Are we going to use Makefile?

3. Error log - Binglan: issues caused by different developing environment
    - Binglan had issue configuring ghostscript for python.
