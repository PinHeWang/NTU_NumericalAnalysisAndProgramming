import numpy as np

def give_me_an_array(n):
    output = np.zeros((n,n), dtype='int64')
### START YOUR CODE HERE ###
    for i in range(n):
        output[i] = np.arange(n)+i+1

#### END YOUR CODE HERE ####
    return output
