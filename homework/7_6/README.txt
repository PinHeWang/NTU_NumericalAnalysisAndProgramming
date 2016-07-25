Implement a function which takes a single Nx1 (N can be any integer > 2) array as the argument, ie.

b = array([[ b1 ],
           [ b2 ],
           [ b3 ],
           [ b4 ],
           ...
           [ bN ]])
Solve for the following linear equations Ax=b, and return the resulting x values ( stored in a Nx1 array).

							A×x=b

[2 1 1 1 ... 1      [x1     [b1
 0 2 1 1 ... 1       x2      b2
 0 0 2 1 ... 1       x3      b3
 0 0 0 2 ... 1   ×   x4  =   b4
 :           :       :       :
 .           .       .       .
 0 0 0 0 ... 2]      xN]     bN]

 As an example, if the input array b is given as following:

b = array([[ 4. ],
           [ 3. ],
           [ 2. ],
           [ 1. ]])
Your output should read like

x = array([[ 0.9375 ],
           [ 0.875  ],
           [ 0.75   ],
           [ 0.5    ]])