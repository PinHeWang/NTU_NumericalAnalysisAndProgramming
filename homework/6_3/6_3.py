import math
import scipy.integrate as integrate

def func(x):
    value = 0.
### START YOUR CODE HERE ###
    for n in range(1,6):
        value += 1 + math.sin(n*math.pi*x)*x + math.cos(n*math.pi*x)*(x**2);

#### END YOUR CODE HERE ####
    return value

def func_integrated(x):
    value = 0.
### START YOUR CODE HERE ###
    value, err = integrate.quad(func,-x,x);
    
#### END YOUR CODE HERE ####
    return value
