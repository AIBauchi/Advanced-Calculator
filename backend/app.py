"""
Start a flask web application that:
listens on 0.0.0.0 port 5000
displays "Hello Dumbass!"
use strict_slashes=Fale
"""
from complex_number import add_complex, div_complex,\
    mul_complex, sub_complex, conjugate, modulus
from Matrix import Matrix
from maths_functions import factorial, ln, log, log10,\
    sin, tan, cos, sqrt, nth_root, combinations, permutations
from NUMBER_SYSTEM import deci, hexa, octal, binary
from flask import Flask, render_template


"""
Start a flask web application that:
listens on 0.0.0.0 port 5000
displays "Hello Dumbass!"
use strict_slashes=Fale
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    returns hello at root call
    """
    # return 'Hello Dumbass!'
    return render_template('index.html')


"""
Routing for solving complex numbers
"""


@app.route('/add_complex/<text>/', strict_slashes=False)
@app.route('/add/<text>/', strict_slashes=False)
def add_comp(text):
    text = text.replace("_", " ")
    text = text.replace("+", " ")
    text = text.split()
    sum = complex(0)
    for i in range(len(text)):
        sum = add_complex(sum, complex(int(text[i][0]), int(text[i][2])))
    return str(sum)


@app.route('/sub_complex/<text>/', strict_slashes=False)
@app.route('/sub/<text>/', strict_slashes=False)
def sub_comp(text):
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = text.split()
    sub = complex(int(text[0][0]), int(text[0][2]))
    text.pop(0)
    for i in range(len(text)):
        sub = sub_complex(sub, complex(int(text[i][0]), int(text[i][2])))
    return str(sub)


@app.route('/mul_complex/<text>/', strict_slashes=False)
@app.route('/mul/<text>/', strict_slashes=False)
def mul_comp(text):
    text = text.replace("_", " ")
    text = text.replace("*", " ")
    text = text.split()
    mul = complex(int(text[0][0]), int(text[0][2]))
    text.pop(0)
    for i in range(len(text)):
        mul = mul_complex(mul, complex(int(text[i][0]), int(text[i][2])))
    return str(mul)


@app.route('/div_complex/<text>/')
@app.route('/div/<text>/')
def div_comp(text):
    text = text.replace("_", " ")
    text = text.replace("/", " ")
    text = text.split()
    div = complex(int(text[0][0]), int(text[0][2]))
    text.pop(0)
    for i in range(len(text)):
        div = div_complex(div, complex(int(text[i][0]), int(text[i][2])))
    return str(div)


@app.route('/mod/<int:text>/', strict_slashes=False)
@app.route('/absolute/<int:text>/', strict_slashes=False)
def absolute(text):
    if type(text) == complex:
        return str(modulus(text))
    return str(modulus(complex(text)))


@app.route('/conjugate/<int:text>/', strict_slashes=False)
def conj(text):
    if type(text) == complex:
        return str(conjugate(text))
    return str(conjugate(complex(text)))


"""
Routing for solving matrices
"""


@app.route('/matrix/<text>/', strict_slashes=False)
def matrices(text):
    text = eval(text)
    if type(text) is list:
        matrix1 = Matrix(text)
        return str(matrix1.determinant())
    matrix1 = text[0]
    matrix2 = text[1]
    matrix1 = Matrix(matrix1)
    matrix2 = Matrix(matrix2)
    sum = matrix1 + matrix2
    diff = matrix1 - matrix2
    prod = matrix1 * matrix2
    return (f'Sum:\t{str(sum)} \nDifference:\t{str(diff)}'
            f'\nProduct:\t{str(prod)}'
            f'\nMatrix1 Det:\t{str(matrix1.determinant())}'
            f'\nMatrix2 Det:\t{str(matrix2.determinant())}')


@app.route('/matrix/how-to/', strict_slashes=False)
def matrix_howto():
    return render_template('matrix_how_to.html')


@app.route('/factorial/<int:n>')
def fact(n):
    return str(factorial(n))


@app.route('/sqrt/<float:n>')
@app.route('/sqrt/<int:n>')
def sqroot(n):
    return str(round(sqrt(n), 2))


@app.route('/nroot/<text>')
def nroot(text):
    text = text.split(',')
    return str(round(nth_root(float(text[0]), int(text[1])), 2))


@app.route('/sin/<int:n>')
@app.route('/sin/<float:n>')
def sine(n):
    return sin(n)


@app.route('/cos/<int:n>')
@app.route('/cose/<float:n>')
def cosine(n):
    return cos(n)


@app.route('/tan/<int:n>')
@app.route('/tan/<float:n>')
def tangent(n):
    return tan(n)


@app.route('/ln/<int:n>')
@app.route('/ln/<float:n>')
def natural_log(n):
    return ln(n)


@app.route('/log10/<int:n>')
@app.route('/logt/<int:n>')
@app.route('/log10/<float:n>')
@app.route('/logt/<float:n>')
def logt(n):
    return log10(n)


@app.route('/log/text')
def logarithm(text):
    text = text.split(',')
    return str(round(log(float(text[0]), int(text[1])), 4))


@app.route('/combination/text')
def combination(text):
    text = text.split(',')
    return str(combinations(int(text[0]), int(text[1])))


@app.route('/permutation/text')
def permutation(text):
    text = text.split(',')
    return str(permutations(int(text[0]), int(text[1])))


@app.route('/hexa/<int:n>')
def hexa_decimal(n):
    return str(hexa(n))


@app.route('/octal/<int:n>')
def octal_decimal(n):
    return str(octal(n))


@app.route('/deci/<text>')
def decimal(text):
    text = text.split(',')
    return str(deci(int(text[0]), int(text[1])))


@app.route('/binary/<int:n>')
def bin(n):
    return str(binary(n))


if __name__ == '__main__':
    app.run('0.0.0.0', '5000')
