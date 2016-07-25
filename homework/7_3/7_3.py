import numpy as np

def give_me_an_array(x):
    output = np.ones_like(x)
### START YOUR CODE HERE ###
    for n in range(1,5):
        output *= np.cos(n*np.pi*x/2)*np.cosh(x) + np.sin(n*np.pi*x/2)*np.sinh(x);

#### END YOUR CODE HERE ####
    return output
