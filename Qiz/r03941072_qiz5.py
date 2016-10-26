

def tree_builder(input):
	output_tree = ''
### START YOUR CODE HERE ###
	output_tree = output_tree + '(-,' + str(input[0]) + ',-)';
	output_tree = output_tree.split(','); # list
	print output_tree
	print len(output_tree)
	print len(output_tree)/2
	
	for i in range(1,len(input)):
		for j in range(len(output_tree)/2):
			if input[i] < output_tree[j]
		
#### END YOUR CODE HERE ####
	return output_tree


tree_builder([314, 159, 265, 35, 89, 79, 323, 84, 62]);