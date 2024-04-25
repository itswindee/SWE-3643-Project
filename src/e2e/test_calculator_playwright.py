import re
from playwright.sync_api import expect, Page

# preq-E2E-TEST-5
def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5000/")
    title = page.title()
    assert "Calculator" in title

def test_add_operation(page: Page):
    page.goto("http://127.0.0.1:5000/")

    # Fill inputs with numeric values
    page.fill('input[name="num1"]', '5')
    page.fill('input[name="num2"]', '3')

    # Click the Add button
    page.click('button:has-text("A + B")')

    # Get the result from the UI
    result = page.text_content('.info-box')

    # Verify the sum displayed in the calculator UI matches Input A plus Input B
    assert result == '5 + 3 = 8'

def test_divide_by_zero_error(page: Page):
    page.goto("http://127.0.0.1:5000/")

    # Fill input A with a value and input B with zero
    page.fill('input[name="num1"]', '10')
    page.fill('input[name="num2"]', '0')

    # Click the Divide button
    page.click('button:has-text("A / B")')

    # Get the result from the UI
    result = page.text_content('.info-box')

    # Verify the result is an error state including a result box containing "Not a Number"
    assert 'Error: Division by zero' in result

def test_invalid_input_error(page: Page):
    page.goto("http://127.0.0.1:5000/")

    # Fill input A with a numeric value and input B with a text value
    page.fill('input[name="num1"]', '10')
    page.fill('input[name="num2"]', 'fifteen')

    # Click the Add button
    page.click('button:has-text("A + B")')

    # Get the result from the UI
    result = page.text_content('.info-box')

    # Verify the last part contains the error message
    assert 'Invalid input. Please enter valid numbers.' in result



def test_clear_button(page: Page):
    page.goto("http://127.0.0.1:5000/")

    # Fill inputs with numeric values
    page.fill('input[name="num1"]', '5')
    page.fill('input[name="num2"]', '3')

    # Click the Add button
    page.click('button:has-text("A + B")')

    # Click the Clear button
    page.click('button:has-text("Clear")')

    # Get the result from the UI
    result = page.text_content('.info-box')

    # Verify the application has returned to the default sta




