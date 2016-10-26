
data = \
    [["ANNUMINAS","FORNOST",12],
     ["FORNOST","ANNUMINAS",12],
     ["FORNOST","GREYHAVENS",39],
     ["FORNOST","HOBBITON",17],
     ["FORNOST","BREE",11],
     ["GREYHAVENS","FORNOST",39],
     ["GREYHAVENS","MICHELDELVING",14],
     ["MICHELDELVING","GREYHAVENS",14],
     ["MICHELDELVING","HOBBITON",2],
     ["MICHELDELVING","THARBAD",31],
     ["HOBBITON","FORNOST",17],
     ["HOBBITON","MICHELDELVING",2],
     ["HOBBITON","BREE",13],
     ["BREE","FORNOST",11],
     ["BREE","HOBBITON",13],
     ["BREE","THARBAD",21],
     ["THARBAD","BREE",21],
     ["THARBAD","MICHELDELVING",31]]

def show_the_shortest_path(start, end):
### START YOUR CODE HERE ###
	d = [None]*7
	visit = [None]*7
	parent = [None]*7

	inf = float('Inf');
	wi0 = [0, 12, inf, inf, inf, inf, inf];
	wi1 = [12, 0, 39, 17, 11, inf, inf];
	wi2 = [inf, 39, 0, inf, inf, 14, inf];
	wi3 = [inf, 17, inf, 0, 13, 2, inf];
	wi4 = [inf, 11, inf, 13, 0, inf, 21];
	wi5 = [inf, inf, 14, 2, inf, 0, 31];
	wi6 = [inf, inf, inf, inf, 21, 31, 0];

	#loc 2 loc distance
	w =[wi0,wi1,wi2,wi3,wi4,wi5,wi6];
	result = ''

	dictionary = {'ANNUMINAS':0, 'FORNOST':1, 'GREYHAVENS':2, 'HOBBITON':3\
		, 'BREE':4, 'MICHELDELVING':5, 'THARBAD':6, 0:'ANNUMINAS', 1:'FORNOST', 2:'GREYHAVENS'\
		, 3:'HOBBITON', 4:'BREE', 5:'MICHELDELVING', 6:'THARBAD'};

	for i in range(7): visit[i] = False;
	for i in range(7): d[i] = 1e9;

	d[dictionary[start]] = 0;
	parent[dictionary[start]] = dictionary[start];

	for k in range(7):
		a = -1;
		b = -1;
		minimum = 1e9;

		for i in range(7):
			if (not visit[i] and d[i] < minimum):
				a = i;
				minimum = d[i];
			
		# check out the relaxation path	
		visit[a] = True;
		for b in range(7):
			if (not visit[b] and d[a]+w[a][b] < d[b]):
				d[b] = d[a] + w[a][b];
				parent[b] = a;
			
	## print out the result
	a = dictionary[end];
	for i in range(100):	
		result += (dictionary[a])[::-1] + ' > ' + 'mk ' + (str(w[a][parent[a]]))[::-1] + ' > '
		a = parent[a];
		if a == dictionary[start]:
			break;
	result += start[::-1]
	
	print 'The shortest path: ' + result[::-1]
	
#### END YOUR CODE HERE ####

show_the_shortest_path("ANNUMINAS","BREE")

