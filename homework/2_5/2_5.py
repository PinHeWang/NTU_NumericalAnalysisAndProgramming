def find_greatest_common_factor(M,N):
    greatest_common_factor = 0
### START YOUR CODE HERE ###
    for x in range(1,M+1):
        if M%x==0:
            if N%x==0:
                greatest_common_factor = x
            else:
                continue
        else:
            continue
                

#### END YOUR CODE HERE ####
    return greatest_common_factor

