def prepare_n_to_mth_tuple(m,n):
    output = ()
### START YOUR CODE HERE ###
    for i in range(1,n+1):
        output = output[:i]+(i**m,);

#### END YOUR CODE HERE ####
    return output

