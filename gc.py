from Bio import SeqIO
#takes a fasta file and parses the sequences 
#returns a dictionary file with the sequence ID as key, sequence as value
def parse_fasta(fasta_file):
	fasta_dict = {}
	fasta_sequences = SeqIO.parse(open(fasta_file), 'fasta')
	for fasta in fasta_sequences:
		name, sequence = fasta.id, str(fasta.seq)
		fasta_dict[name] = sequence
	return fasta_dict


#given a dna string, return percentage of string that is G or C
def gc_content(dna_string):
	# count all instances of G and C
	full_count = dna_string.count("G") + dna_string.count("C")
	# convert into a percentage. cast to float due to python int math
	percentage = (float(full_count) / len(dna_string))*100
	return percentage


def perc_conv(dict):
	percentage_dict = dict.copy()
	for x in dict.keys():
		percentage_dict[x] = gc_content(dict.get(x))
	return percentage_dict

#given a dictionary of percentages, return key of highest
def highest_perc(dict):
	tmp_list = dict.values()
	tmp_list.sort()
	return tmp_list[-1]

def gc(file):
	bp_dict = parse_fasta(file)
	new_dict = perc_conv(bp_dict)
	tmp = highest_perc(new_dict)
	val = {}
	for key in new_dict.keys():
		if new_dict[key] == tmp :
			val = (key, round(new_dict[key], 6))

	return val


print gc('rosalind_gc.txt')
	