def legendre(n, x):
### IMPLEMENT YOUR CODE BELOW ###
    if n > 1:
        y = 0.5*((2*n-1)*x**n - (2*n-3)*x**(n-2));
    else:
        y = x**n
    
        
    return y

