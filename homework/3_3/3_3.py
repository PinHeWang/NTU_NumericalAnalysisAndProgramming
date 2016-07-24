import datetime

def days_since_special_relativity_paper(year,month,day):
    days = 0
### START YOUR CODE HERE ###
    y = year;
    m = month;
    d = day;
    day = datetime.datetime(y,m,d) - datetime.datetime(1905,9,26);
    days = day.days;
            
        
#### END YOUR CODE HERE ####
    return days

