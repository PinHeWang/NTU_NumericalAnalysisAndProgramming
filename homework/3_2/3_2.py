import math

def evaluate_equation(x,y,t):
    ret_value = 1.
### START YOUR CODE HERE ###
    for n in range(1,5):
        ret_value *= math.cos(n*math.pi*t/2)*math.cosh(x)+math.sin(n*math.pi*t/2)*math.sinh(y)
        
#### END YOUR CODE HERE ####
    return ret_value

