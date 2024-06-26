from flask import Flask, render_template, request
import math

app = Flask(__name__, template_folder='../flaskr/templates')


@app.route('/')
def index():
    return render_template('index.html')


def perform_calculation(num1, num2, operation):
    result = None
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = 'Error: Division by zero'
            else:
                result = num1 / num2
        elif operation == 'equals':
            result = 1 if abs(num1 - num2) < 1e-9 else 0
        elif operation == 'power':
            result = num1 ** num2
        elif operation == 'log':
            if num1 <= 0 or num2 <= 0:
                result = 'Error: Invalid input'
            else:
                result = math.log(num1) / math.log(num2)
        elif operation == 'root':
            if num2 == 0:
                result = 'Error: Division by zero'
            else:
                result = num1 ** (1 / num2)
        elif operation == 'factorial':
            result = factorial(num1)
        elif operation == 'sin':
            result = round(math.sin(num1 * math.pi / 180), 8)
        elif operation == 'cos':
            result = round(math.cos(num1 * math.pi / 180), 8)
        elif operation == 'tan':
            result = round(math.tan(num1 * math.pi / 180), 8)
        elif operation == 'reciprocal':
            if num1 == 0:
                result = 'Error: Division by zero'
            else:
                result = 1 / num1
        else:
            result = 'Invalid operation'
    except (ValueError, ZeroDivisionError):
        result = 'Error: Invalid input'

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    return result


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        operation = request.form['operation']
        num2 = None
        if 'num2' in request.form and request.form['num2']:
            num2 = float(request.form['num2'])
    except ValueError:
        return 'Invalid input. Please enter valid numbers.'

    try:
        result = perform_calculation(num1, num2, operation)
    except ValueError:
        if operation in ['log', 'root'] and (num1 <= 0 or num2 <= 0):
            result = 'Error: Invalid input'
        else:
            result = 'Error: Calculation error'

    return str(result)

def factorial(num):
    if num < 0:
        return -factorial(abs(num))
    if num == 0:
        return 1
    return num * factorial(num - 1)


if __name__ == '__main__':
    app.run(debug=True)



