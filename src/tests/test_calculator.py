import pytest
from src.calculator_engine.calculator import perform_calculation, factorial





def test_invalid_operation():
    result = perform_calculation(2, 3, 'invalid')
    assert result == 'Invalid operation'



 # preq-UNIT-TEST-2
def test_addition():
    assert perform_calculation(2, 3, '+') == 5
    assert perform_calculation(-2, 3, '+') == 1
    assert perform_calculation(0, 0, '+') == 0
    assert perform_calculation(2.5, 3.5, '+') == 6.0
    assert perform_calculation(0, 3, '+') == 3
    assert perform_calculation(-2, -3, '+') == -5

# preq-UNIT-TEST-3
def test_subtraction():
    assert perform_calculation(5, 3, '-') == 2
    assert perform_calculation(-2, 3, '-') == -5
    assert perform_calculation(0, 0, '-') == 0
    assert perform_calculation(0, 3, '-') == -3
    assert perform_calculation(2.5, 1.5, '-') == 1.0

# preq-UNIT-TEST-4
def test_multiplication():
    assert perform_calculation(2, 3, '*') == 6
    assert perform_calculation(-2, 3, '*') == -6
    assert perform_calculation(0, 0, '*') == 0
    assert perform_calculation(2.5, 3.5, '*') == 8.75
    assert perform_calculation(0, 3, '*') == 0

# preq-UNIT-TEST-5
def test_division():
    assert perform_calculation(6, 3, '/') == 2.0
    assert perform_calculation(5, 2, '/') == 2.5
    assert perform_calculation(5, 0, '/') == 'Error: Division by zero'
    assert perform_calculation(0, 5, '/') == 0.0

# preq-UNIT-TEST-6
def test_division_error():
    assert perform_calculation(5, 0, '/') == 'Error: Division by zero'
    assert perform_calculation(-6, 0, '/') == 'Error: Division by zero'
    assert perform_calculation(6, 0.0, '/') == 'Error: Division by zero'

# preq-UNIT-TEST-7
def test_equals():
    assert perform_calculation(5, 5, 'equals') == 1
    assert perform_calculation(5, 6, 'equals') == 0

# preq-UNIT-TEST-8
def test_power():
    assert perform_calculation(2, 3, 'power') == 8
    assert perform_calculation(5, 0, 'power') == 1
    assert perform_calculation(0, 5, 'power') == 0
    assert perform_calculation(2, -3, 'power') == 0.125

# preq-UNIT-TEST-9
def test_log():
    assert perform_calculation(1, 10, 'log') == 0.0
    assert perform_calculation(0, 10, 'log') == 'Error: Invalid input'
    assert perform_calculation(-1, 10, 'log') == 'Error: Invalid input'
    assert perform_calculation(1, 10, 'log') == 0

# preq-UNIT-TEST-10
def test_log_error_1():
    assert perform_calculation(0, 2, 'log') == 'Error: Invalid input'
    assert perform_calculation(-2, 2, 'log') == 'Error: Invalid input'
    assert perform_calculation(0, -10, 'log') == 'Error: Invalid input'

# preq-UNIT-TEST-11
def test_log_error_2():
    assert perform_calculation(1, 10, 'log') == 0.0
    assert perform_calculation(-10, 0, 'log') == 'Error: Invalid input'

# preq-UNIT-TEST-12
def test_root():
    assert perform_calculation(8, 3, 'root') == 2.0
    assert perform_calculation(8, 0, 'root') == 'Error: Division by zero'
    assert perform_calculation(8, 3, 'root') == 2

# preq-UNIT-TEST-13
def test_root_error():
    assert perform_calculation(8, 0, 'root') == 'Error: Division by zero'
    assert perform_calculation(-8, 0, 'root') == 'Error: Division by zero'

# preq-UNIT-TEST-14
def test_factorial():
    assert perform_calculation(5, 0, 'factorial') == 120
    assert perform_calculation(0, 0, 'factorial') == 1
    assert perform_calculation(-5, 0, 'factorial') == -120

# preq-UNIT-TEST-15
def test_factorial_convention():
    assert perform_calculation(0, None, 'factorial') == 1
    assert perform_calculation(-1, None, 'factorial') == -1

# preq-UNIT-TEST-16
def test_sin():
    assert perform_calculation(30, 0, 'sin') == 0.5
    assert perform_calculation(90, 0, 'sin') == 1.0
    assert perform_calculation(180, 0, 'sin') == 0.0
    assert perform_calculation(30, None, 'sin') == pytest.approx(0.5)

# preq-UNIT-TEST-17
def test_cos():
    assert perform_calculation(30, 0, 'cos') == 0.8660254
    assert perform_calculation(90, 0, 'cos') == 0.0
    assert perform_calculation(180, 0, 'cos') == -1.0
    assert perform_calculation(60, None, 'cos') == pytest.approx(0.5)

# preq-UNIT-TEST-18
def test_tan():
    assert perform_calculation(45, 0, 'tan') == 1.0
    assert perform_calculation(135, 0, 'tan') == -1.0
    assert perform_calculation(0, 0, 'tan') == 0.0
    assert perform_calculation(45, None, 'tan') == pytest.approx(1)

# preq-UNIT-TEST-19
def test_reciprocal():
    assert perform_calculation(2, 0, 'reciprocal') == 0.5
    assert perform_calculation(0, 0, 'reciprocal') == 'Error: Division by zero'
    assert perform_calculation(-2, 0, 'reciprocal') == -0.5

# preq-UNIT-TEST-20
def test_reciprocal_error():
    assert perform_calculation(0, None, 'reciprocal') == 'Error: Division by zero'
    assert perform_calculation(-0.5, None, 'reciprocal') == -2






