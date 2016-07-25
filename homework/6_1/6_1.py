import math
import scipy.misc as misc

def func(x):
    value = 1.
### START YOUR CODE HERE ###
    for n in range(1,5):
        value *= math.cos(n*math.pi*x/2)*math.cosh(x) + math.sin(n*math.pi*x/2)*math.sinh(x);

#### END YOUR CODE HERE ####
    return value

def func_first_derivative(x):
    value = 1.
### START YOUR CODE HERE ###
    value = misc.derivative(func,x,1e-5);

#### END YOUR CODE HERE ####
    return value
