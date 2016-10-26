
def dihkstra(source,end):

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

	d[dictionary[source]] = 0;
	parent[dictionary[source]] = dictionary[source];

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
		if a == dictionary[source]:
			break;
	result += source[::-1]
	
	print 'The shortest path: ' + result[::-1]




	
		
## Example
dihkstra('ANNUMINAS','BREE')



