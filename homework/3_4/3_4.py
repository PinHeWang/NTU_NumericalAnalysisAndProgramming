import random

def password_generator():
    password = ''
### START YOUR CODE HERE ###
    l = 'abcdefghijklmnopqrstuvwxyz'
    u = l.upper();
    n = '0123456789';
    s = list(l) + list(u) + list(n);
    s = ''.join(s)

    #print s
    #print type(s)
    
    for i in range(10):
    	password += random.choice(s)
    

#### END YOUR CODE HERE ####
    return password

print password_generator()

