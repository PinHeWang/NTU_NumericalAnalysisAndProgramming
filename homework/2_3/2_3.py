def calculate_sum_of_factors(N):
    sum_of_factors = 0
### START YOUR CODE HERE ###
    for x in range(1,N+1):
        if N%x==0:
            sum_of_factors += x
        else:
            continue
            
                

#### END YOUR CODE HERE ####
    return sum_of_factors

