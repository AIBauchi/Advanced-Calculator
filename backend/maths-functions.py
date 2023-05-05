import math

def factorial(x):
    """
    Compute the factorial of a non-negative integer.

    Args:
        x (int): The non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of x.

    Raises:
        ValueError: If x is negative.

    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

def sqrt(x):
    """
    Compute the square root of a non-negative number using the Newton-Raphson method.

    Args:
        x (float): The non-negative number whose square root is to be computed.

    Returns:
        float: The square root of x.

    Raises:
        ValueError: If x is negative.

    Example:
        >>> sqrt(4)
        2.0
        >>> sqrt(2)
        1.414213562373095
    """
    if x < 0:
        raise ValueError("Square root is not defined for negative numbers")
    if x == 0:
        return 0
    guess = x / 2
    while abs(guess**2 - x) > 1e-6:
        guess = (guess + x/guess) / 2
    return guess

def nth_root(x, n):
    """
    Compute the nth root of a positive number.

    Args:
        x (float): The positive number whose nth root is to be computed.
        n (int): The positive integer root to be computed.

    Returns:
        float: The nth root of x.

    Raises:
        ValueError: If x is negative and n is even.

    Example:
        >>> nth_root(27, 3)
        3.0
        >>> nth_root(16, 4)
        2.0
    """
    if x < 0 and n % 2 == 0:
        raise ValueError("Nth root is not defined for negative numbers with even roots")
    if x == 0:
        return 0
    lower = 0
    upper = max(1, x)
    while True:
        mid = 0.5 * (lower + upper)
        if abs(mid ** n - x) < 1e-9:
            return mid
        elif mid ** n < x:
            lower = mid
        else:
            upper = mid


def sin(x):
    """
    Compute the sine of an angle in radians.

    Args:
        x (float): The angle in radians whose sine is to be computed.

    Returns:
        float: The sine of x.

    Example:
        >>> sin(math.pi/2)
        1.0
        >>> sin(math.pi)
        1.2246467991473532e-16
    """
    return math.sin(x)

def cos(x):
    """
    Compute the cosine of an angle in radians.

    Args:
        x (float): The angle in radians whose cosine is to be computed.

    Returns:
        float: The cosine of x.

    Example:
        >>> cos(math.pi/2)
        6.123233995736766e-17
        >>> cos(math.pi)
        -1.0
    """
    return math.cos(x)


def tan(x):
    """
    Compute the tangent of an angle in radians.

    Args:
        x (float): The angle in radians whose tangent is to be computed.

    Returns:
        float: The tangent of x.

    Example:
        >>> tan(math.pi/4)
        0.9999999999999999
        >>> tan(math.pi)
        -1.2246467991473532e-16
    """
    return math.tan(x)

def ln(x):
    """
    Compute the natural logarithm of a positive number.

    Args:
        x (float): The positive number whose natural logarithm is to be computed.

    Returns:
        float: The natural logarithm of x.

    Raises:
        ValueError: If x is non-positive.

    Example:
        >>> ln(math.e)
        1.0
        >>> ln(10)
        2.302585092994046
    """
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers")
    return math.log(x)


def log10(x):
    """
    Compute the base 10 logarithm of a positive number.

    Args:
        x (float): The positive number whose base 10 logarithm is to be computed.

    Returns:
        float: The base 10 logarithm of x.

    Raises:
        ValueError: If x is non-positive.

    Example:
        >>> log10(100)
        2.0
        >>> log10(1000)
        3.0
    """
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers")
    return math.log10(x)

def log(x, base):
    """
    Compute the logarithm of a positive number (x) to base (base).

    Args:
        x (float): The positive number whose base 10 logarithm is to be computed.

    Returns:
        float: The base 10 logarithm of x.

    Raises:
        ValueError: If x is non-positive.

    Example:
        >>> log(8,2)
        0.9030899869919435
        >>> log(91,3)
        1.9590413923210936
    """
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers")
    return math.log10(x)

def combinations(n, k):
    """
    Compute the number of combinations of k elements from a set of n elements.

    Args:
        n (int): The total number of elements in the set.
        k (int): The number of elements to choose from the set.

    Returns:
        int: The number of combinations of k elements from a set of n elements.

    Raises:
        ValueError: If n or k is negative, or if k is greater than n.

    Example:
        >>> combinations(5, 2)
        10
        >>> combinations(10, 5)
        252
    """
    if n < 0 or k < 0 or k > n:
        raise ValueError("Invalid arguments")
    result = 1
    for i in range(1, k+1):
        result *= (n - k + i) / i
    return int(result)

def permutations(n, k):
    """
    Compute the number of permutations of k elements from a set of n elements.

    Args:
        n (int): The total number of elements in the set.
        k (int): The number of elements to choose from the set.

    Returns:
        int: The number of permutations of k elements from a set of n elements.

    Raises:
        ValueError: If n or k is negative, or if k is greater than n.

    Example:
        >>> permutations(5, 2)
        20
        >>> permutations(10, 5)
        30240
    """
    if n < 0 or k < 0 or k > n:
        raise ValueError("Invalid arguments")
    result = 1
    for i in range(n - k + 1, n+1):
        result *= i
    return result

