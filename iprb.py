from decimal import *

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
	#print len_pop
	pair_list = list()
	if len_pop < 2:
		return "Unable to process populations less than 2"
	for i in range(len_pop-1):
		for j in range(i+1, len_pop):
			pair_list.append(pop[i]+pop[j]) 
	return pair_list

def pair_perc(pair):
	switcher = {
		"kk":1,
		"km":1,
		"kn":1,
		"mm":.75,
		"mn":.50,
		"nn":0
	}
	return switcher.get(pair, "nothing")

def perc_list(pairs):
	perc = list()
	for i in pairs:
		perc.append(pair_perc(i))
	return perc

def iprb(k,m,n):
	pairs = make_pairs(pop2list(k,m,n))
	p_list = perc_list(pairs)
	for i in range(len(p_list)):
		p_list[i] = Decimal(p_list[i]) * (Decimal(1)/Decimal(len(p_list)))
	return sum(p_list)


print iprb(15,30,22)