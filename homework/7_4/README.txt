Implement a function which takes three squared arrays (of shape NxN) A, B, and C. The function should return the output of the following equation:

f(A, B, C) = A^2 + B^2 + C^2 - A*B - B*C - C*A + 4I

As an example, if the input arrays A, B, C are given as following:

A = array([[1., 2.],
           [3., 4.]])

B = array([[3., 2.],
           [4., 1.]])

C = array([[2., 4.],
           [1., 3.]])
Your output should read like

array([[ 3., -4.],
       [-8.,  5.]])