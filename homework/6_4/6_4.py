import math
import scipy.integrate as integrate

def prob_at_nsigma(n):
    prob = 0.
### START YOUR CODE HERE ###
    G = lambda x : (1/math.sqrt(2*math.pi))*math.exp(-(x**2)/2);
    prob,err = integrate.quad(G,-n,n)

#### END YOUR CODE HERE ####
    return prob
