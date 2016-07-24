Following up the previous exercise again --- extend your legendre(n,x) function to support even higher order polynomials based on the Bonnet's recursion formula:

(n+1)P_n+1(x) = (2n+1)xP_n(x) - nP_n-1(x)

Now the argument n can be any non-negtive integers, and the function should still return the nth order Legendre polynomial of x.