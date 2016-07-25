import numpy as np

def give_me_an_array(n):
    output = np.zeros((10,10), dtype='int64')
### START YOUR CODE HERE ###
    x = np.kron(np.eye(5),np.rot90(np.eye(2)))
    y = np.kron(np.rot90(np.eye(5)),np.eye(2))
    
    i = np.kron(np.eye(4),np.rot90(np.eye(2)))
    j = np.kron(np.rot90(np.eye(4)),np.eye(2))
    
    i = np.concatenate((np.zeros((8,1)),i), axis=1)
    i = np.concatenate((i,np.zeros((8,1))), axis=1)
    i = np.concatenate((np.zeros((1,10)),i))
    i = np.concatenate((i,np.zeros((1,10))))

    j = np.concatenate((np.zeros((8,1)),j), axis=1)
    j = np.concatenate((j,np.zeros((8,1))), axis=1)
    j = np.concatenate((np.zeros((1,10)),j))
    j = np.concatenate((j,np.zeros((1,10))))

    output = x+y+i+j
    output[output==1]=n
#### END YOUR CODE HERE ####
    return output
