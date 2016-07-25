import numpy as np
import scipy.linalg as linalg

def give_me_an_array(A, B, C):
    output = np.zeros((2,2))
### START YOUR CODE HERE ###
    output[0,0] = linalg.det(A+B.dot(linalg.inv(C)))
    output[0,1] = linalg.det(B-C.dot(linalg.inv(A)))
    output[1,0] = linalg.det(B-A.dot(linalg.inv(C)))
    output[1,1] = linalg.det(A+C.dot(linalg.inv(B)))

#### END YOUR CODE HERE ####
    return output
