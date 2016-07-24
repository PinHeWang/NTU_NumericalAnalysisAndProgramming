def check_with_monkeys(A, B, C):
    flag = True
### START YOUR CODE HERE ###
    if A >= B and B >= C:
        flag = True
    elif B >= A+C or C >= A+B or A >= B+C:
        flag = True
    else:
        flag = False

#### END YOUR CODE HERE ####
    return flag

