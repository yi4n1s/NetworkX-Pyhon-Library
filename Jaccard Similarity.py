#The Jaccard Similarity implementation in python using the NetworkX library.

def jaccard_similarity(x,y):
	
	intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
	union_cardinality = len(set.union(*[set(x), set(y)]))
	return intersection_cardinality/float(union_cardinality)