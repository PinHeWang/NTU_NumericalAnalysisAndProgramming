import numpy as np
import scipy.linalg as linalg

def give_me_an_array(b):
    output = np.zeros_like(b)
### START YOUR CODE HERE ###
    s,s1 = np.shape(b)
    A = np.diag(np.diag(np.ones((s,s)))) + np.triu(np.ones((s,s)))
    output = (linalg.inv(A)).dot(b)
    
#### END YOUR CODE HERE ####
    return output
