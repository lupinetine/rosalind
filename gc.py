from Bio import SeqIO
def parse_fasta(fasta_file):
	fasta_dict = {}
	fasta_sequences = SeqIO.parse(open(fasta_file), 'fasta')
	for fasta in fasta_sequences:
		name, sequence = fasta.id, str(fasta.seq)
		fasta_dict[name] = sequence
	return fasta_dict



def gc_content(dna_string):
	full_count = float(dna_string.count("G")) + float(dna_string.count("C"))
	percentage = full_count / len(dna_string)
	return percentage


def gc(file):
	bp_dict = parse_fasta(file)
	percentage_dict = bp_dict.copy()
	for x in bp_dict.keys():
		percentage_dict[x] = gc_content(bp_dict.get(x))
	return percentage_dict


print gc('rosalind_gc_example.txt')
	