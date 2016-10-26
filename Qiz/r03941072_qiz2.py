
def parallelogram_word(input):
### START YOUR CODE HERE ###
    s = ' '*(len(input)-1) + input + ' '*(len(input)-1);
    #print s[6];
    #print s[7];
    for i in range(len(input)*2-1):
    	t = '';
    	for j in range(i,i+len(input)):
    		t += s[j];
        print t;
    print '\n'

input = raw_input('Input a arbitrary string: ');
parallelogram_word(input);
#### END YOUR CODE HERE ####