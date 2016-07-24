source = '''
Name    HW#1  HW#2  HW#3  HW#4  Midterm  FinalExam
James   10     6     8    10     90       85	
Mary     9     8     9     9     78       80
Keith    7     7     8     7     92       82 
Bruce    9     6     9    10     85       88
Kim      7     6     9     8     64       72
Emma    10     9     7     6     95       85
Cathy    6     7     7    10     73       77'''

### START YOUR CODE BELOW ###
James = source[source.find('James'):source.find('Mary')]
Mary = source[source.find('Mary'):source.find('Keith')]
Keith = source[source.find('Keith'):source.find('Bruce')]
Bruce = source[source.find('Bruce'):source.find('Kim')]
Kim = source[source.find('Kim'):source.find('Emma')]
Emma = source[source.find('Emma'):source.find('Cathy')]
Cathy = source[source.find('Cathy'):]

James = James.split('  ')
Mary = Mary.split('  ')
Keith = Keith.split('  ')
Bruce = Bruce.split('  ')
Kim = Kim.split('  ')
Emma = Emma.split('  ')
Cathy = Cathy.split('  ')

Javg = (int(James[1]) + int(James[3]) + int(James[5]) + int(James[7]))*1 + (int(James[9])+int(James[12]))*0.3
Mavg = (int(Mary[2]) + int(Mary[4]) + int(Mary[6]) + int(Mary[8]))*1 + (int(Mary[10])+int(Mary[13]))*0.3
Kavg = (int(Keith[2]) + int(Keith[4]) + int(Keith[6]) + int(Keith[8]))*1 + (int(Keith[10])+int(Keith[13]))*0.3
Bavg = (int(Bruce[2]) + int(Bruce[4]) + int(Bruce[6]) + int(Bruce[8]))*1 + (int(Bruce[10])+int(Bruce[13]))*0.3
Kimavg = (int(Kim[3]) + int(Kim[5]) + int(Kim[7]) + int(Kim[9]))*1 + (int(Kim[11])+int(Kim[14]))*0.3
Eavg = (int(Emma[2]) + int(Emma[4]) + int(Emma[6]) + int(Emma[8]))*1 + (int(Emma[10])+int(Emma[13]))*0.3
Cavg = (int(Cathy[2]) + int(Cathy[4]) + int(Cathy[6]) + int(Cathy[8]))*1 + (int(Cathy[10])+int(Cathy[13]))*0.3

Javg = round(Javg)
Mavg = round(Mavg)
Kavg = round(Kavg)
Bavg = round(Bavg)
Kimavg = round(Kimavg)
Eavg = round(Eavg)
Cavg = round(Cavg)

print 'Name    Average'
print James[0]+'   '+str(Javg)
print Mary[0]+'    '+str(Mavg)
print Keith[0]+'   '+str(Kavg)
print Bruce[0]+'   '+str(Bavg)
print Kim[0]+'     '+str(Kimavg)
print Emma[0]+'    '+str(Eavg)
print Cathy[0]+'   '+str(Cavg)


