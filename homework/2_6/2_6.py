def find_least_common_multiple(M,N):
    least_common_multiple = 0
### START YOUR CODE HERE ###
    for x in range(1,M+1):
        if M%x==0:
            if N%x==0:
                least_common_multiple = x*(M/x)*(N/x)
            else:
                continue
        else:
            continue

#### END YOUR CODE HERE ####
    return least_common_multiple

