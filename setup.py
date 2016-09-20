"""
Created by Nathan Buckner
"""

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="needle-in-haystack",
    version="0.0.4",
    description="Needle in haystack interview question",
    long_description=read("README.md"),
    author="Nathan Buckner",
    author_email="dropbox255@gmail.com",
    url="http://github.com/bucknerns/needle_in_haystack",
    py_modules=["needle"],
    include_package_data=True,
    install_requires=read("pip-requires").split("\n"),
    license=read("LICENSE"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python"])
