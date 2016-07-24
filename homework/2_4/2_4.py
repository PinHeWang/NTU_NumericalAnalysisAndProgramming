def calculate_sum_of_prime_factors(N):
    sum_of_prime_factors = 0
### START YOUR CODE HERE ###
    for x in range(2,N):
        if N%x==0:
            for y in range(2,x):
                if x%y==0:
                    break
            else:
                sum_of_prime_factors += x
        else:
            continue
#### END YOUR CODE HERE ####
    return sum_of_prime_factors

