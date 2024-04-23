import sys
from src.calculator_engine.app import perform_calculation, factorial
sys.path.append('path_to_src_directory')
import pytest


# preq-UNIT-TEST-2
def test_addition():
    assert perform_calculation(2, 3, '+') == 5

# preq-UNIT-TEST-3
def test_subtraction():
    assert perform_calculation(5, 2, '-') == 3

# preq-UNIT-TEST-4
def test_multiplication():
    assert perform_calculation(5, 2, '*') == 10

# preq-UNIT-TEST-5
def test_division():
    assert perform_calculation(6, 2, '/') == 3

# preq-UNIT-TEST-6
def test_division_error():
    assert perform_calculation(5, 0, '/') == 'Error: Division by zero'


# preq-UNIT-TEST-7
    def test_equals():
        assert perform_calculation(5, 5, 'equals') == 1

# preq-UNIT-TEST-8
def test_power():
    assert perform_calculation(2, 3, 'power') == 8

# preq-UNIT-TEST-9
def test_log():
    assert perform_calculation(8, 2, 'log') == 3.0

# preq-UNIT-TEST-10
def test_log_error_1():
    assert perform_calculation(0, 10, 'log') == 'Error: Invalid input'

# preq-UNIT-TEST-11
def test_log_error_2():
    assert perform_calculation(1, 10, 'log') == 0.0

# preq-UNIT-TEST-12
def test_root():
    assert perform_calculation(8, 3, 'root') == 2.0

# preq-UNIT-TEST-13
def test_root_error():
    assert perform_calculation(8, 0, 'root') == 'Error: Division by zero'

# preq-UNIT-TEST-14
def test_factorial():
    assert factorial(5) == 120

# preq-UNIT-TEST-15
def test_factorial_convention():
    assert perform_calculation(0, None, 'factorial') == 1

# preq-UNIT-TEST-16
def test_sin():
    assert perform_calculation(30, None, 'sin') == 0.5

# preq-UNIT-TEST-17
def test_cos():
    assert perform_calculation(60, None, 'cos') == 0.5

# preq-UNIT-TEST-18
def test_tan():
    assert perform_calculation(45, None, 'tan') == 1.0


# preq-UNIT-TEST-19
def test_reciprocal():
    assert perform_calculation(5, None, 'reciprocal') == 0.2

# preq-UNIT-TEST-20
def test_reciprocal_error():
    assert perform_calculation(0, None, 'reciprocal') == 'Error: Division by zero'
