sum_of_series = 0.
### START YOUR CODE HERE ###

for n in range(100):
    n += 1
    if n % 2 == 0:
        n = float((-1)**(n+1)) / (n)
        sum_of_series += n
    else:
        n = float((-1)**(n+1)) / (n)
        sum_of_series += n

#### END YOUR CODE HERE ####
print 'value:', sum_of_series
