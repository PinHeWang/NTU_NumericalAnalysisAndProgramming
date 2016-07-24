def legendre(n, x):
### IMPLEMENT YOUR CODE BELOW ###
    if n == 0 or n == 1:
        return x**n;
    else:
        return (2-1./n)*x*legendre(n-1,x)-(1-1./n)*legendre(n-2,x);

