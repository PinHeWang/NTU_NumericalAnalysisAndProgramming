E=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
EE = E+E

def English(x):
	K = ''
	for y in range(x,26+x):
		K += EE[y]
	print K

for x in range(26):
	English(x)