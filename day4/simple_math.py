""" A collection of simple math operations.

Functions to compute basic arithmetic, and polynomials up to order 2.
"""
def simple_add(a,b):
    """ Add two numbers.

    Parameters
    ----------
    a : int, float
        First term.
    b : int, float
        Second term
    
    Returns
    -------
    int, float
        The sum of a and b.
    """
    return a+b

def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
