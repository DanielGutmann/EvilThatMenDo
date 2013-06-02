
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "EvilThatMenDo",
    version = "0.0.1",
    author = "Chris Perivolaropoulos",
    author_email = "darksaga2006@gmail.com",
    description = ("Living on the razor's edge, balancing on a ledge"),
    license = "GPL",
    keywords = "",
    url = "http://packages.python.org/EvilThatMenDo",
    packages=['evilthatmendo', 'evilthatmendo.test'],
    install_requires=['pillow', 'numpy', 'scipy'],
    tests_require=['nose'],
    long_description=read('README.org'),
    test_suite='evilthatmendo.test',
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)"
    ],
)
