
# TRREASURE_IMAGE
> TRREASURE_IMAGE is a python third-party library  with Command-Line Interface[cli] feature.



## Table of Contents
* [General Info](#general-information)
* [Python library Used](#Python-library-used)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [To do](#to-do)
* [Contact](#contact)
* [License](#license)
 


## General Information
>You can do some awesome things like hide anything in a .jpg image or
>even make a gif from normal images with two lines of code or covert text files and images.

What can you do with it?
- can hide secret messages or executable file or images and share by another image.
- can easily make gifs using photos for free
- can convert images and text files also


## Python library Used
- language info: python - version 3+
- python standard libraries - [ logging, io, os, pathlib, argparse]
- python third-party libraries - Pillow(version 8.3.2)


## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.


## Usage
- To hide someting in a jpg file you have to user the PIRATE module like below, 
``` 
from treasure_image import PIRATE

#if want to hide a string in example.jpg(host image)
PIRATE.hide_str_treasure(image="example.jpg", treasure="This is a hidden message!")

#if want to hide a image in example.jpg(host image)
PIRATE.hide_img_treasure(image="example.jpg", treasure="hidden_image.png")

#if want to hide a file(.exe, .py, .cpp, .txt etc) in example.jpg(host image)
PIRATE.hide_file_treasure(image="example.jpg", treasure="hidden_file.exe")
```


## Project Status
Project is: _in progress_


## To do

- Support for image formats as host image (currently jpg is allowed)
- Support for vector graphics (.svg, .ai etc)


## Contact
Created by [@FatinShadab](https://github.com/FatinShadab) - feel free to contact me!

<!-- Optional -->
## License
 This project is open source and available under the [MIT License]().
