def insert_sum_between_two_digits(input):
    output = ''
### START YOUR CODE HERE ###
    for i in range(4):
        output = '';
        for j in range(len(input)-1):
            output += input[j] + str(int(input[j])+int(input[j+1]));
        output += input[len(input)-1];
        input = output

#### END YOUR CODE HERE ####
    return output

