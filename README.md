# PythonTest
Develop Python Test
![Pytest_logo svg](https://github.com/user-attachments/assets/abdd6d4b-009a-4ce0-9d07-8936c43ef9d9)

# Unit Testing in Python
The three most popular test runners in Python are:

# unittest
Built into the Python standard library.
python3 -m pydoc unittest
major requirements of unittest:

Tests are written in a class which inherits from unittest.TestCase.
Forced to use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement
# nose or nose2
$ pip install nose2

Nose's tagline is "nose extends unittest to make testing easier".

nose is compatible with any tests written using the unittest framework and can be used as a drop-in replacement for the unittest test runner. The development of nose as an open-source application fell behind, and a fork called nose2 

# pytest
$ pip install pytest

pytest supports execution of unittest test cases. pytest test cases are a series of functions in a Python file starting with the name test_. Despite the fact that it reduces boilerplate code to the minimum, it still remains readable.

Other great features of pytest:

Support for the built-in assert statement instead of using special self.assert*() methods
Auto-discovery of test modules and functions
Support for filtering of test cases
Ability to rerun from the last failing test
An ecosystem of hundreds of plugins to extend the functionality

# Pytest vs Unittest

https://www.browserstack.com/guide/pytest-vs-unittest


