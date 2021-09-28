
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
- To hide extract something from a jpg file you have to user the EXPLORER module like below,
``` 
from treasure_image import EXPLORER

#if want to extract a string from example.jpg(host image)
EXPLORER.seek_str_treasure(image="example.jpg")

#if want to extract a image from example.jpg(host image)
EXPLORER.seek_img_treasure(image="example.jpg")
# it has two more default parameters which are 'save' and 'treasure_format',
#
# save=True(default) it saves the image in local machine
# if save=False than it only shows the image.
# treasure_format='jpg'(default) if save=True it saves the file in provided treasure_format.

#if want to extract a .exe file from example.jpg(host image)
EXPLORER.seek_exe_treasure(image="example.jpg")
# there is a default perameter 'treasure_name'
# treasure_name='treasure.exe'(default) saves the exe file in the provided name and format.

#if want to extract a script/files from example.jpg(host image)
EXPLORER.seek_file_treasure(image="example.jpg")
# it has two more default parameters which are 'treasure_name' and 'treasure_format',
#
# treasure_name="treasure"(default) it saves the file with provided name
# treasure_format='text'(default) if save=True it the file/script in provided format/type.
```

## Project Status
Project is: _in progress_
>Any kind of Support will be appreciate.


## To do

- Support for image formats as host image (currently jpg is allowed)
- Support for vector graphics (.svg, .ai etc)


## Contact
Created by [@FatinShadab](https://github.com/FatinShadab) - feel free to contact me!

<!-- Optional -->
## License
 This project is open source and available under the [MIT License](https://github.com/FatinShadab/TRREASURE_IMAGE/blob/main/LICENSE).
