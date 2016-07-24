def prepare_poker_deck():
    deck = [None]*53
### START YOUR CODE HERE ###
    number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']; #13
    suit = ['CLUB','DIAMOND','HEART','SPADE']; #4
    for i in range(1,53):
        if i>=1 and i<=13:
            deck[i] = suit[0] + '-' + number[(i-1)%13];
        elif i>13 and i<=26:
            deck[i] = suit[1] + '-' + number[(i-1)%13];
        elif i>26 and i<=39:
            deck[i] = suit[2] + '-' + number[(i-1)%13];
        elif i>39 and i<=52:
            deck[i] = suit[3] + '-' + number[(i-1)%13];
    del deck[0]
#### END YOUR CODE HERE ####
    return deck

