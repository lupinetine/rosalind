def revc(dna):
	dna = dna[::-1]
	revc = list()
	for x in range(len(dna)):
		revc.append(base_swap(dna[x]))
	return "".join(revc)

def base_swap(base):
	switcher = {
		"A": "T",
		"T": "A",
		"C": "G",
		"G": "C"
	}
	return switcher.get(base, "nothing")


print revc("GACGTAAGTTACCGATATGACGGATAAGTAACACAACTTAGGATAAGCGCTTAAAGGAGTTGTGATACTGCGACGCCGATAACTTAGCTCGATAACAATGCGAGCGACTGCCCACGATCTATTGGGCAAGGGGACATCACGGTTGTTGGTTTCTTTCTCCAGGCCAGCCATCTGAGTCTCGTACGCGGTCATAGTACTCCGTAAGGTGTACTTTGATTGGCGCGCGGACCAAGTTACCGCGGCTCTCGGCTCCACCGTACGGCGACACAACTTAACTGAGTTTGGAAGATCTACCTATCAAGCTTGACCCAGTGTATAGTTATGTGTTTATAACTGTCGCTTAGTATCACGGGCCGCTCTGTAGATGAACTCTCACGTGAGGGCCTGTCATGCGCATCATGGTGTGATTGCACGAGCCTATCGAAAGGGACGGTACCAGGGCATTGCTGACTGGATGTCAGACACGAGTCTGATTCATGCCGGTGTGCCTTAGTTCTATAAACCCAGCTCTTATGCACACTCATAGTCCGTACGGAGACGGCCGAAATCCGCAGACAGGAATAACTTTGTGGCGGGTAGAAAAGCAGACGCCAGAGTCCAGGAACCCGCAGGCCTGTGACGACCACGAGCATTTTGGGGGTACCCGCTGCACCCGCTGGCAGCCCCTCGGGCTACTAGGGATGCTCGTGTAGTGAAAGCACGAGTTTTAGGCTAATAGAGTCTGTTATGGGCTTCCGGTTCTAGCCCATTCCTCACCGGGTACACGCAATGCAGTGATCCCATGGTAGATCAATAGACCATAAGTACCAGAACGGTATGCG")