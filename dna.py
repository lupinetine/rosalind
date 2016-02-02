def dna_count(dna):
	count_list = list()
	count_dict = {"A":0, "C":0, "G":0, "T":0
	}
	#count A
	count_list.append(dna.count("A"))
	count_list.append(dna.count("C"))
	count_list.append(dna.count("G"))
	count_list.append(dna.count("T"))
	return count_list

#print dna_count("GATACATA")