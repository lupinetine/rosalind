import dna
from Bio import SeqIO
import numpy as np
#takes a fasta file and parses the sequences 
#returns a dictionary file with the sequence ID as key, sequence as value
def parse_fasta(fasta_file):
	fasta_dict = {}
	fasta_sequences = SeqIO.parse(open(fasta_file), 'fasta')
	for fasta in fasta_sequences:
		name, sequence = fasta.id, str(fasta.seq)
		fasta_dict[name] = sequence
	return fasta_dict

def bp_by_position(dict):
	bps = []
	temp_string = ""
	for i in range(len(dict[dict.keys()[0]])):
		for k in dict.keys():
			temp_string += dict[k][i]
		bps.append(dna.dna_count(temp_string))
		temp_string = ""
	return bps

#returns a string with the base and the number at each index i.e. "A: 5 2 3"
def bp_cons_builder(bp_list, string, pos): 
	for i in range(len(bp_list)):
		string += (str(bp_list[i][pos]) + " ")
	return string

#return the base that is associated with the index number given
def list_index_to_bp(index):
	switcher = {
		0: "A",
		1: "C",
		2: "G",
		3: "T"
	}
	return switcher.get(index, "nothing")

#print parse_fasta('rosa_consensus_example.txt')

new = bp_by_position(parse_fasta('rosalind_cons.txt'))
#print new

a_string = bp_cons_builder(new, "A: ", 0)
c_string = bp_cons_builder(new, "C: ", 1)
g_string = bp_cons_builder(new, "G: ", 2)
t_string = bp_cons_builder(new, "T: ", 3)



cons_string = ""
for i in range(len(new)):
	cons_string += list_index_to_bp(new[i].index(max(new[i])))

print cons_string

print a_string
print c_string
print g_string
print t_string