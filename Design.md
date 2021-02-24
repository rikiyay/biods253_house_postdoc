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
2. We will run a local web server using Docker to receive users' input.
3. Create a python program that receives users' input to draw an image of a nice looking house. 

**Phase I**

For now, the image of house will have the following fixed components.
- 4 windows
- 2 garage doors
- 1 door
- 2 trees
- 1 clouds

**Phase II**

Allow users to specify different numbers of objects in the image of a house.

### Non-Goals

1. We won't draw a castle.
2. We won't host a web server from AWS.
3. We will not support choices of alternative colors.

### Future goals

1. Host an interactive web interface from AWS.

## Detailed Design

We will have a `Python-cli` that accepts integer numbers of windows, garage doors, house doors, trees, and clouds as arguments (Only allow integers for any arguments) from users. There will be a checkpoint that validates whether input arguments are integers. If not, the program returns an error and exit. If inputs are integers, the program will invoke functions in the `python_lib` to draw an image. 

We will have a `python_lib` that defines class(es) or functions to create house objects using Turtle.


### User requirements

1. need to have a python=3.8 environment 
1. need to specify minimum and maximum number of objects.
- 0 <= windows <= _ (set a default value = 4)
- 0 <= garage doors <= _ (set a default value = 2)
- 1 <= doors <= _ (set a default value = 1). You must have at least one door to get in or out of a house.
- 0 <= trees <= _ (set a default value = 2)
- 0 <= clouds <= _ (set a default value = 1)

### New/changed data structures?

N/A

### What APIs will you use/change?

N/A

### Throughput/latency/cost/efficiency concerns?

N/A

### Data validation/what are potential error states?

Non-integer arguments -> Return error.

### Logging/monitoring/observability

N/A

### Security/Privacy

N/A

### What will you test?

TBD (depending on what functions we will implement)

## Third Party dependencies

- Python (>= 3, tested on version 3.8.7)
- Pre-built python library "turtle".

## Work Estimates

This project is due Feb 28 (Sun).

## Alternative Approaches

N/A

## Homework Logging

1. We have different ways of using python and python packages. 
- Binglan will use pyenv (and venv) for python = 3.8.7 (Binglan's default version)
- Rikiya will use conda for python=3.8.5 (conda only allowed me to install 3.8.5, so we have a little compatibility issue here -> docker may be a good solution but will try to see how the current setting works)

1. Question from Rikiya: Are we going to use Makefile?

1. Next step is to
- Get familiar with turtle
- Draw an overview of our house in some shared doc (google slide, draw.io, etc.)? 
    - Binglan - I'd like to try out draw.io for this project.