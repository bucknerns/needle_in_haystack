"""
Created by Nathan Buckner
"""

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# Establish a consistent base directory relative to the setup.py file
os.chdir(os.path.abspath(os.path.dirname(__file__)))


# tox integration
class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="needle-in-haystack",
    version="0.0.5",
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
        "Programming Language :: Python"],
    tests_require=read("test-requires").split(),
    cmdclass={'test': Tox})
