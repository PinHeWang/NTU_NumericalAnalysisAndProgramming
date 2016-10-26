

palindromic_number_100th = 0
palindromic_number_1000th = 0

### START YOUR CODE HERE ###
def checkP(n):
	s, i = str(n), 0 
	j = len(s) - 1 
	while (j - i > 0): 
		if (s[i] != s[j]): 
			return False 
		i += 1 
		j -= 1 
	return True

def generate(n): 
	n=n+10
	result = 0 
	while n > 0: 
		if checkP(result): 
			n -= 1 
		result += 1 
	return result - 1

palindromic_number_100th = generate(100)
palindromic_number_1000th = generate(1000)
#### END YOUR CODE HERE ####

print 'The 100th palindromic number:', palindromic_number_100th
print 'The 1000th palindromic number:', palindromic_number_1000th