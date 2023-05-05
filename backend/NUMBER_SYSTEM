
def binary(x):
    """
    This function takes a positive integer as input and returns its binary representation.

    Args:
        x (int): The positive integer to be converted to binary.

    Returns:
        int: The binary representation of x.

    Raises:
        ValueError: If x is not a positive integer.

    Example:
        >>> binary(10)
        1010
    """
    if x<=0:
        raise ValueError("Invalid Input")
    else:
        b=""
        x = int(x)
        r=0
        while r==0 or r==1:
            r=x%2
            x = x/2
            b=str(int(r))+b
        b=int(b)
    return b


def deci(x,y):
    """
    This function takes a number and a base as input and returns the decimal representation of the number.

    Args:
        x (int): The number to be converted to decimal.
        y (int): The base of the number.

    Returns:
        int: The decimal representation of the number.

    Raises:
        ValueError: If x is not a positive integer.

    Example:
        >>> deci(1010, 2)
        10
    """
    if x<=0:
        raise ValueError("Invalid Input")
    else:
        if y==16:
            sx=str(x)
            l = len(sx)-1
            n = 0
            for m in sx:
                if m =="A":
                    m=10*(y**(l))
                    n=n+m
                elif m == "B":
                    m=11*(y**(l))
                    n=n+m
                elif m == "C":
                    m=12*(y**(l))
                    n=n+m
                elif m == "D":
                    m=13*(y**(l))
                    n=n+m
                elif m == "E":
                    m=14*(y**(l))
                    n=n+m
                elif m == "F":
                    m=15*(y**(l))
                    n=n+m
                else:
                    k=int(m)
                    n = n + (k * (y**(l)))
                l=l-1
            return n
        else: 
            sx=str(x)
            l = len(sx)
            n = 0
            for i in sx:
                k=int(i)
                n = n + (k * (y**(l-1)))
                l=l-1
            return n




def octal(x):
    """
    This function takes a positive integer as input and returns its octal representation.

    Args:
        x (int): The positive integer to be converted to octal.

    Returns:
        int: The octal representation of x.

    Raises:
        ValueError: If x is not a positive integer.

    Example:
        >>> octal(10)
        12
    """
    if x<=0:
        raise ValueError("Invalid Input")
    else:
        o=""
        x = int(x)
        r=0
        while r==0 or r>=1:
            r=x%8
            x = x/8
            o=str(int(r))+o
        o=int(o)  
        return o



def hexa(x):
    """
    This function takes a positive integer as input and returns its hexadecimal representation.

    Args:
        x (int): The positive integer to be converted to hexadecimal.

    Returns:
        str: The hexadecimal representation of x.

    Raises:
        ValueError: If x is not a positive integer.

    Example:
        >>> hexa(255)
        'FF'
    """
    if x<=0:
        raise ValueError("Invalid Input")
    else:
        h=""
        x = int(x)
        while (x>=1):
            r=x%16
            x = x//16
            if r>=10:
                if r == 10:
                    h="A"+h 
                if r == 11:
                    h="B"+h
                if r == 12:
                    h="C"+h
                if r == 13:
                    h="D"+h
                if r == 14:
                    h="E"+h   
                if r == 15:
                    h="F"+h
            else:
                h=str(int(r))+h
        return h






