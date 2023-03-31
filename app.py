#simple calculator using flask framework
from flask import Flask, render_template, request
app = Flask(__name__)
#define render_template to render html file
@app.route('/')
def index():
    return render_template('index.html')
#function to add two numbers
def add(num1, num2):
    return num1 + num2
#function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2
#function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
#function to divide two numbers
def divide(num1, num2):
    return num1 / num2
#function to calculate the result
@app.route('/result', methods=['POST'])
def result():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operation = request.form['operation']
    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    return render_template('result.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)











