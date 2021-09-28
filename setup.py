import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

VERSION = "1.0.0"
DESCRIPTION = "hide data(strings, images, files, scripts etc) into image, make gifs, covert images and files etc"

#This call to setup() does all the work
setup(
    name ="Treasure-Image",
    version = VERSION,
    description = DESCRIPTION,
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/FatinShadab/TRREASURE_IMAGE",
    author="Fatin Shadab",
    author_email = "fatinshadab123@gmail.com",
    license = "MIT",
    keywords=['python', 'image', 'hide image', 'hide exe', 'image hack', 'converter', 'image converter', 'gifs'],
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages = find_packages(),
    include_package_data = True,
    install_requires = ['Pillow'],
)
