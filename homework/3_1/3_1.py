import math
func = 0.
### START YOUR CODE HERE ###
for m in range(1,4):
    for n in range(1,4):
        func+=m*(math.pi)**n
        
func = math.log(func)

#### END YOUR CODE HERE ####
print 'value:',func