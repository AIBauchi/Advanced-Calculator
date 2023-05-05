## MATH-FUNCTIONS FILE

* The code in the `maths-functions.py` provided contains a series of mathematical functions written in Python. Each function takes one or more inputs and returns a result based on a specific mathematical operation.

* The `factorial(x)` function takes a non-negative integer x and returns the factorial of that number. If x is negative, a ValueError is raised.

* The `sqrt(x)` function takes a non-negative number x and returns the square root of that number using the Newton-Raphson method. If x is negative, a ValueError is raised.

* The `nth_root(x, n)` function takes a positive number x and a positive integer n and returns the nth root of x. If x is negative and n is even, a ValueError is raised.

* The `sin(x)` function takes an angle in radians x and returns the sine of that angle.

* The `cos(x)` function takes an angle in radians x and returns the cosine of that angle.

* The `tan(x)` function takes an angle in radians x and returns the tangent of that angle.

* The `ln(x)` function takes a positive number x and returns the natural logarithm of that number. If x is non-positive, a ValueError is raised.

* The `log10(x)` function takes a positive number x and returns the base 10 logarithm of that number. If x is non-positive, a ValueError is raised.

* The `log(x, base)` function takes a positive number x and a positive base base and returns the logarithm of x to the base base. If x is non-positive, a ValueError is raised.
## NUMBER_SYSTEM FILE
The code in the `number-systems.py` file contains a series of functions for converting numbers between different number systems.

* The `binary(x)` function takes a positive integer x and returns its binary representation as a string. If x is non-positive, a ValueError is raised.

* The `octal(x)` function takes a positive integer x and returns its octal representation as a string. If x is non-positive, a ValueError is raised.

* The `hexa(x)` function takes a positive integer x and returns its hexadecimal representation as a string. If x is non-positive, a ValueError is raised.

* The `deci(x, y)` function takes a positive integer x and a positive integer y representing the original number system, and returns the decimal equivalent of the number. If x is non-positive or y is not a valid base, a ValueError is raised.

Each of these functions takes specific input(s) and returns specific output(s) based on the mathematical operation of converting between different number systems. The docstrings for each function provide more detail on the specific requirements for input(s) and output(s) and raise ValueErrors for any invalid inputs.
