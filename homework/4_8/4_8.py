def isFullHouse(cards):
    flag = True
### START YOUR CODE HERE ###
    a = [None]*len(cards);
    for i in range(len(cards)):
        a[i] = (cards[i])[len(cards[i])-1];
    # check
    for j in range(len(a)):
        if a.count(a[j])<2:
            flag = False;
            break;
            

#### END YOUR CODE HERE ####
    return flag

