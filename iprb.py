def pop2list(k,m,n):
	pop_list = list()
	for i in range(k):
		pop_list.append("k")
	for i in range(m):
		pop_list.append("m")
	for i in range(n):
		pop_list.append("n")
	return pop_list

def make_pairs(pop):
	len_pop = len(pop)
	print len_pop
	pair_list = list()
	if len_pop < 2:
		return "Unable to process populations less than 2"
	for i in range(len_pop-1):
		for j in range(i+1, len_pop):
			pair_list.append(pop[i]+pop[j]) 
	return pair_list



def iprb(k,m,n):
	p_list = pop2list(k,m,n)
	pairs = make_pairs(p_list)
	print pairs

print iprb(2,2,2)