import dna
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


print parse_fasta('rosa_consensus_example.txt')