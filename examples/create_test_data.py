"""MIT License
Copyright (c) 2025 Christian Hågenvik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


EXAMPLE:
This example demonstrates how to create test data for a calculator function using the `pytest` framework and the `testing` module from the `chtoolbox` package.
Functions:
    calculator(a, b, operation): Performs basic arithmetic operations (add, subtract, multiply, divide) based on the given operation.
    test_calculator(): Runs tests on the calculator function using generated test data and asserts the correctness of the results.
Modules:
    chtoolbox.testing: Provides utilities for creating test cases and generating test results.
Example Usage:
    The test_calculator function can be run with the `pytest` command in the terminal or by running the function directly in the Python interpreter.
Assumptions:
    The example assumes that the calculator function is working correctly and that the user wants to generate automatic tests that can be implemented to ensure that the function continues to work as expected.
"""

# 


# This is my function, in which I want to create some test data for testing using the `pytest` framework
def calculator(a, b, operation):
    if operation == 'add':
        return a+b
    elif operation == 'subtract':
        return a-b
    elif operation == 'multiply':
        return a*b
    elif operation == 'divide':
        return a/b
    else:
        raise ValueError('Invalid operation')

# Import the testing module from the chtoolbox package
from chtoolbox import testing

# Create a dictionary with test cases that contains all combinations of the input lists
# NB: The keys in the dictionary must match the input arguments of the function you want to test
cases = testing.create_test_cases(
    {'a': [1, 2, 3, 4],
     'b': [5, 6, 7, 8],
     'operation': ['add', 'subtract', 'multiply', 'divide']
     }
)

# Generate dictionary with test data, containing both input to tests and expected output (based on your function)
# The print_cases argument prints the test cases to the console
test_data = testing.generate_test_results(calculator, cases, print_cases=True)

# The test_data dictionary can now be used as input to tests in the `pytest` framework
# For example, you can loop through the dictionary and run tests like this:
def test_calculator():
    for key, value in test_data.items():
        assert calculator(**value['input']) == value['output'], f"Test case {key} failed"
    
    print('All test cases passed')

# The test_calculator function can be run with the `pytest` command in the terminal
# Or by running the function directly in the Python interpreter
test_calculator()