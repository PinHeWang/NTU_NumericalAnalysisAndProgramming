Following up the previous exercise --- instead of implementing an independent function for each polynomial, write a single function legendre(n,x) which takes two arguments, an integer n and a float point number x. The argument n can be equal to 0, 1, 2, or 3, and the function should return the nth order Legendre polynomial of x. ie.

P(n=0,x) = 1
P(n=1,x) = x
P(n=2,x) = 0.5*((3x^2)-1)
P(n=3,x) = 0.5*((5x^3)-3x)