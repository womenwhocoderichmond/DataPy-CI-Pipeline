import os
import io
from setuptools import setup, find_packages
from os import path
from io import open

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name='SimpleRestApp',  # Required


# To print absolute path on your system
# os.path.abspath('.')

# To print files and directories in the current directory
# on your system
# os.listdir('.')


    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.3.0',  # Required
    #def __path(filename):
    #return os.path.join(os.path.dirname(__file__),
    #                    filename)

    url="https://github.com/womenwhocoderichmond/DataPy-CI-Pipeline",
    packages=find_packages()
    )
