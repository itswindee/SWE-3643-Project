import re
from playwright.sync_api import expect, Page

# preq-E2E-TEST-5
def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5000/")
    title = page.title()
    assert "Calculator" in title

# preq-E2E-TEST-6
def test_add_operation(page: Page):
    page.goto("http://127.0.0.1:5000/")

    # fill inputs with numeric values
    page.fill('input[name="num1"]', '5')
    page.fill('input[name="num2"]', '3')

    # clicking the add button
    page.click('button:has-text("A + B")')

    # get the result from the UI
    result = page.text_content('.info-box')

    # verify the sum displayed in the calculator UI matches Input A plus Input B
    assert result == '5 + 3 = 8'

# preq-E2E-TEST-7
def test_divide_by_zero_error(page: Page):
    page.goto("http://127.0.0.1:5000/")

    # fill input A with a value and input B with zero
    page.fill('input[name="num1"]', '10')
    page.fill('input[name="num2"]', '0')

    # clicking the divison button
    page.click('button:has-text("A / B")')

    # get the result from the UI
    result = page.text_content('.info-box')

    # verify the result is an error state including a result box containing "Not a Number"
    assert 'Error: Division by zero' in result

# preq-E2E-TEST-8
def test_invalid_input_error(page: Page):
    page.goto("http://127.0.0.1:5000/")

    # fill input A with a numeric value and input B with a text value
    page.fill('input[name="num1"]', '10')
    page.fill('input[name="num2"]', 'fifteen')

    # clicking the add button
    page.click('button:has-text("A + B")')

    # get the result from the UI
    result = page.text_content('.info-box')

    # verify the last part contains the error message
    assert 'Invalid input. Please enter valid numbers.' in result


# preq-E2E-TEST-9
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





