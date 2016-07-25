Similar to the previous assignment, implement a function which takes three squared arrays (of shape NxN) A, B, and C. The function should return the following matrix in the formant of 2x2 NumPy array:

[|A+(B/C)|  |B-(C/A)|
 |B-(A/C)   |A+(C/B)|]

As an example, if the input arrays A, B, C are given as following:

A = array([[1., 2.],
           [3., 4.]])

B = array([[3., 2.],
           [4., 1.]])

C = array([[2., 4.],
           [1., 3.]])
Your output should read like

array([[3.5, -1.5],
       [4.5,  7.8]]) 