import subprocess

import pytest
from src.calculator_engine.calculator import perform_calculation, app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calculate_valid_input(client):
    # arrange & act
    response = client.post('/calculate', data=dict(num1='2', operation='+', num2='3'))

    # assert
    assert response.status_code == 200
    assert b"5" in response.data

def test_calculate_invalid_input(client):
    # arrange & act
    response = client.post('/calculate', data=dict(num1='a', operation='+', num2='3'))

    # assert
    assert response.status_code == 200
    assert b"Invalid input. Please enter valid numbers." in response.data

def test_calculate_invalid_operation(client):
    # arrange & act
    response = client.post('/calculate', data=dict(num1='2', operation='invalid', num2='3'))

    # assert
    assert response.status_code == 200
    assert b"Invalid operation" in response.data

def test_calculate_error(client):
    # arrange & act
    response = client.post('/calculate', data=dict(num1='2', operation='log', num2='0'))

    # assert
    assert response.status_code == 200
    assert b"Error: Invalid input" in response.data


def test_invalid_operation():
    # arrange & act
    result = perform_calculation(2, 3, 'invalid')

    # assert
    assert result == 'Invalid operation'


 # preq-UNIT-TEST-2
def test_addition():
    # arrange
    num1, num2, operation = 2, 3, '+'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 5

    assert perform_calculation(2, 3, '+') == 5
    assert perform_calculation(-2, 3, '+') == 1
    assert perform_calculation(0, 0, '+') == 0
    assert perform_calculation(2.5, 3.5, '+') == 6.0
    assert perform_calculation(0, 3, '+') == 3
    assert perform_calculation(-2, -3, '+') == -5


# preq-UNIT-TEST-3
def test_subtraction():
    # arrange
    num1, num2, operation = 5, 3, '-'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 2


    assert perform_calculation(5, 3, '-') == 2
    assert perform_calculation(-2, 3, '-') == -5
    assert perform_calculation(0, 0, '-') == 0
    assert perform_calculation(0, 3, '-') == -3
    assert perform_calculation(2.5, 1.5, '-') == 1.0

# preq-UNIT-TEST-4
def test_multiplication():
    # arrange
    num1, num2, operation = 2, 3, '*'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 6

    assert perform_calculation(2, 3, '*') == 6
    assert perform_calculation(-2, 3, '*') == -6
    assert perform_calculation(0, 0, '*') == 0
    assert perform_calculation(2.5, 3.5, '*') == 8.75
    assert perform_calculation(0, 3, '*') == 0

# preq-UNIT-TEST-5
def test_division():
    # arrange
    num1, num2, operation = 6, 3, '/'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 2.0

    assert perform_calculation(6, 3, '/') == 2.0
    assert perform_calculation(5, 2, '/') == 2.5
    assert perform_calculation(5, 0, '/') == 'Error: Division by zero'
    assert perform_calculation(0, 5, '/') == 0.0

# preq-UNIT-TEST-6
def test_division_error():
    # arrange
    num1, num2, operation = 5, 0, '/'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 'Error: Division by zero'

    assert perform_calculation(5, 0, '/') == 'Error: Division by zero'
    assert perform_calculation(-6, 0, '/') == 'Error: Division by zero'
    assert perform_calculation(6, 0.0, '/') == 'Error: Division by zero'

# preq-UNIT-TEST-7
def test_equals():
    # arrange
    num1, num2, operation = 5, 5, 'equals'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 1

    assert perform_calculation(5, 5, 'equals') == 1
    assert perform_calculation(5, 6, 'equals') == 0

# preq-UNIT-TEST-8
def test_power():
    # arrange
    num1, num2, operation = 2, 3, 'power'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 8

    assert perform_calculation(2, 3, 'power') == 8
    assert perform_calculation(5, 0, 'power') == 1
    assert perform_calculation(0, 5, 'power') == 0
    assert perform_calculation(2, -3, 'power') == 0.125

# preq-UNIT-TEST-9
def test_log():
    # arrange
    num1, num2, operation = 1, 10, 'log'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 0.0

    assert perform_calculation(1, 10, 'log') == 0.0
    assert perform_calculation(0, 10, 'log') == 'Error: Invalid input'
    assert perform_calculation(-1, 10, 'log') == 'Error: Invalid input'
    assert perform_calculation(1, 10, 'log') == 0

# preq-UNIT-TEST-10
def test_log_error_1():
    # arrange
    num1, num2, operation = 0, 2, 'log'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 'Error: Invalid input'

    assert perform_calculation(0, 2, 'log') == 'Error: Invalid input'
    assert perform_calculation(-2, 2, 'log') == 'Error: Invalid input'
    assert perform_calculation(0, -10, 'log') == 'Error: Invalid input'

# preq-UNIT-TEST-11
def test_log_error_2():
    # arrange
    num1, num2, operation = -10, 0, 'log'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 'Error: Invalid input'

    assert perform_calculation(1, 10, 'log') == 0.0
    assert perform_calculation(-10, 0, 'log') == 'Error: Invalid input'

# preq-UNIT-TEST-12
def test_root():
    # arrange
    num1, num2, operation = 8, 3, 'root'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 2.0

    assert perform_calculation(8, 3, 'root') == 2.0
    assert perform_calculation(8, 0, 'root') == 'Error: Division by zero'
    assert perform_calculation(8, 3, 'root') == 2

# preq-UNIT-TEST-13
def test_root_error():
    # arrange
    num1, num2, operation = -8, 0, 'root'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 'Error: Division by zero'

    assert perform_calculation(8, 0, 'root') == 'Error: Division by zero'
    assert perform_calculation(-8, 0, 'root') == 'Error: Division by zero'

# preq-UNIT-TEST-14
def test_factorial():
    # arrange
    num1, num2, operation = 5, 0, 'factorial'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 120

    assert perform_calculation(5, 0, 'factorial') == 120
    assert perform_calculation(0, 0, 'factorial') == 1
    assert perform_calculation(-5, 0, 'factorial') == -120

# preq-UNIT-TEST-15
def test_factorial_convention():
    # arrange
    num1, num2, operation = 0, None, 'factorial'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 1

    assert perform_calculation(0, None, 'factorial') == 1
    assert perform_calculation(-1, None, 'factorial') == -1

# preq-UNIT-TEST-16
def test_sin():
    # arrange
    num1, num2, operation = 30, 0, 'sin'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 0.5

    assert perform_calculation(30, 0, 'sin') == 0.5
    assert perform_calculation(90, 0, 'sin') == 1.0
    assert perform_calculation(180, 0, 'sin') == 0.0
    assert perform_calculation(30, None, 'sin') == pytest.approx(0.5)

# preq-UNIT-TEST-17
def test_cos():
    # arrange
    num1, num2, operation = 30, 0, 'cos'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 0.8660254

    assert perform_calculation(30, 0, 'cos') == 0.8660254
    assert perform_calculation(90, 0, 'cos') == 0.0
    assert perform_calculation(180, 0, 'cos') == -1.0
    assert perform_calculation(60, None, 'cos') == pytest.approx(0.5)

# preq-UNIT-TEST-18
def test_tan():
    # arrange
    num1, num2, operation = 45, 0, 'tan'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 1.0

    assert perform_calculation(45, 0, 'tan') == 1.0
    assert perform_calculation(135, 0, 'tan') == -1.0
    assert perform_calculation(0, 0, 'tan') == 0.0
    assert perform_calculation(45, None, 'tan') == pytest.approx(1)

# preq-UNIT-TEST-19
def test_reciprocal():
    # arrange
    num1, num2, operation = 2, 0, 'reciprocal'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 0.5

    assert perform_calculation(2, 0, 'reciprocal') == 0.5
    assert perform_calculation(0, 0, 'reciprocal') == 'Error: Division by zero'
    assert perform_calculation(-2, 0, 'reciprocal') == -0.5

# preq-UNIT-TEST-20
def test_reciprocal_error():
    # arrange
    num1, num2, operation = 0, None, 'reciprocal'

    # act
    result = perform_calculation(num1, num2, operation)

    # assert
    assert result == 'Error: Division by zero'

    assert perform_calculation(0, None, 'reciprocal') == 'Error: Division by zero'
    assert perform_calculation(-0.5, None, 'reciprocal') == -2






