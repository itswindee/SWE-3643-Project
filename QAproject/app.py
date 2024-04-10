from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    elif operation == 'power':
        result = num1 ** num2
    elif operation == 'log':
        result = math.log(num1, num2)
    elif operation == 'root':
        result = num1 ** (1 / num2)
    elif operation == 'factorial':
        result = math.factorial(num1)
    elif operation == 'sin':
        result = math.sin(num1)
    elif operation == 'cos':
        result = math.cos(num1)
    elif operation == 'tan':
        result = math.tan(num1)
    elif operation == 'reciprocal':
        result = 1 / num1
    elif operation == 'clear':
        result = ''
    else:
        result = 'Invalid operation'

    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
