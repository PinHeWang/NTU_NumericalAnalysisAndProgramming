def track_projectile(m, v0, theta, t):
    x = y = 0.
### START YOUR CODE HERE ###
    import math
    x = v0*math.cos(theta)*t;
    #if t < (v0*math.sin(theta)/9.8):
    y = 0.5*(-9.8)*t**2 + v0*math.sin(theta)*t;
    


#### END YOUR CODE HERE ####
    return x, y

