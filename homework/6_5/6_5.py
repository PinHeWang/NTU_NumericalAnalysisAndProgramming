import math
import scipy.integrate as integrate

def convoluted_BreitWigner(E, M, Gamma, sigma):
    value = 0.
### START YOUR CODE HERE ###
    f = lambda x :  (1/(((E-x)**2-M**2)**2 + (M**2)*(Gamma**2))) * math.exp(-(x**2)/2/(sigma**2));
    value, err = integrate.quad(f,-3*sigma,3*sigma);

#### END YOUR CODE HERE ####
    return value
