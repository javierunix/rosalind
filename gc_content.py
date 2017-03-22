# program to calculate the Guanine and Citosine content of a give DNA sequence

def gc_content(sequence):
	gc_num = 0
	for i in range(0, len(sequence)):
		if sequence[i] == 'C' or sequence[i] == 'G':
			gc_num += 1
	return float(gc_num) / len(sequence) * 100 # we have to convert integers into floating point numbers in order to have a accurate division

dna = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
print gc_content(dna)
