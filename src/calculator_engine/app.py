from flask import Flask, render_template, request
import math

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    return render_template('web/index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
    except ValueError:
        return 'Invalid input. Please enter valid numbers.'

    result = ''
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == 'equals':
        result = 1 if abs(num1 - num2) < 1e-9 else 0
    elif operation == 'power':
        result = num1 ** num2
    elif operation == 'log':
        result = num1 / num2
    elif operation == 'root':
        result = round(num1 ** (1 / num2))
    elif operation == 'factorial':
        result = factorial(int(num1))
    elif operation == 'sin':
        result = round(math.sin(num1 * math.pi / 180), 8)
    elif operation == 'cos':
        result = round(math.cos(num1 * math.pi / 180), 8)
    elif operation == 'tan':
        result = round(math.tan(num1 * math.pi / 180), 8)
    elif operation == 'reciprocal':
        result = 1 / num1
    else:
        result = 'Invalid operation'

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



