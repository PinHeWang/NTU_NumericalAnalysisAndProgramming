import numpy as np

def give_me_an_array(A, B, C):
    output = np.zeros_like(A)
### START YOUR CODE HERE ###
    s1, s2 = np.shape(A)
    output = A.dot(A) + B.dot(B) + C.dot(C) - A.dot(B) - B.dot(C) - C.dot(A) + 4*np.identity(s1);

#### END YOUR CODE HERE ####
    return output
