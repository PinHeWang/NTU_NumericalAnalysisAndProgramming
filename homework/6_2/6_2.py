import math
import scipy.misc as misc

def func(x):
    value = 1.
### START YOUR CODE HERE ###
    value = x**2 + math.exp(x) + math.log(x) + math.sin(x);

#### END YOUR CODE HERE ####
    return value

def func_2nd_derivative_numerical(x):
    value = 1.
### START YOUR CODE HERE ###
    value = misc.derivative(func,x,1e-5,2);

#### END YOUR CODE HERE ####
    return value

def func_2nd_derivative_analytical(x):
    value = 1.
### START YOUR CODE HERE ###
    value = 2 + math.exp(x) - 1/(x**2) - math.sin(x);

#### END YOUR CODE HERE ####
    return value
