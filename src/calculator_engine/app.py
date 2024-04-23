from flask import Flask, render_template, request
import math

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    return render_template('index.html')


def perform_calculation(num1, num2, operation):
    pass


@app.route('/calculate', methods=['POST'])
def calculate(num1, num2, operation):
    try:
        num1 = float(request.form['num1'])
        operation = request.form['operation']
        if 'num2' in request.form and request.form['num2']:
            num2 = float(request.form['num2'])
    except ValueError:
        return 'Invalid input. Please enter valid numbers.'

    result = perform_calculation(num1, num2, operation)
    return str(result)

    result = ''
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
        result = num1 ** (1 / num2)
    elif operation == 'log':
        result = math.log(num1) / math.log(num2);
    elif operation == 'root':
        result = round(num1 ** (1 / num2))
    elif operation == 'factorial':
        result = -1 * factorial(-num1) if num1 < 0 else factorial(num1)
    elif operation == 'sin':
        result = round(math.sin(num1 * math.pi / 180), 8)
    elif operation == 'cos':
        result = round(math.cos(num1 * math.pi / 180), 8)
    elif operation == 'tan':
        result = round(math.tan(num1 * math.pi / 180), 8)
        result = round(result, 8)
    elif operation == 'reciprocal':
        if num1 == 0:
            result = 'Error: Division by zero'
        else:
            result = 1 / num1
    else:
        result = 'Invalid operation'

    if isinstance(result, float):
        if result.is_integer():
            result = int(result)


    return render_template('index.html', result='Result: ' + str(result))

def factorial(num):
    if num < 0:
        return 'Invalid input'
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == '__main__':
    app.run(debug=True)



