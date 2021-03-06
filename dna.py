# program for counting the number of nucleotides of each type in a given
# dna sequence

dna = "AAGAACACTGGCAATTTTGCGGAAGGGAGCGTCGCCACTAGCCTGTGGTCTATCGCAACAGACAACGACCGGACAAAGCGCAATGGCTGCCCCTCGAGTGCGGATACTCTCCTATGCTTTTGAGCGTACACAAAGGCGTGCGCAAGGTGGCAGTCAAGAAACGGGGCGTAGTGTCTGCCGACTTAGCCGTGGTGATTAGGGTAAATCCTGCGCTGGTAGAATCGAGCCATCTCATGTGCAGTAGCCATCGACTGAGGAGATCGTCGACAACCAATCGTTGTAGCTTCCCCGTCCGAACGGAGCAAGAGTCCTCCTGTCCTGGTTTGACAACGGCGACCAAACTAAGGAGCTAGTTGGTTGGACCGTGTCAACTGTCTGCTCCCGAGCAGATGCTCTAGTAGTTAGTCGTTCATTGACGATAGTGGTTGGAGTGCACCTATTATGGGTAACGGATTTGGGGCTTCCTCAAGGCATATGTGTGTCTGTTCCGTTTAGCATTCCGCGTAAAGGGTATTATGCGCTAACGTGAAGCGTAAAATTTCAGGACGCAATAATAGTACAAGAAGCAGATAGTCCGCGTGTTGTCGTCTATACTCTTTCAGCGAATCCTGACATGTACTTTAAAGTCCGGCTCTACCGCACTGAGACGGTTTATTAGAAAGTACCGTTGAAACAACGTAGATCTTTTGTTCATCTACCATCTCAGCTCGGAAATTTCTTCATCTTCATATTCCGTGCAACCGGACGTAGGGTGCTGATAGGCAGCTGGCGGGACCCAGATAAGGGGCATCCTGTCGGAGTGACGGCTTAGGTATGCGCTTCACTTATACTTGAGTTATGGTGGCCATCAAAGCCCGACCGGGAGTACTCATCGCAGGGGAGACCTGTGGAACGGCCGTCTCGGTACCATCCGCGTTTAGCGCCAATAGGCATCTGTCGTCCAATTGTGTACCATCTAGGCACGGGCCCCATTTACCAGGTGAAACTGTCT" # input dna sequence
num_A = 0 # number of Adenines
num_C = 0 # number of Citosines
num_G = 0 # number of Guanines
num_T = 0 # number of Timines

for i in range(0, len(dna)):
	if dna[i] == 'A':
		num_A += 1
	if dna[i] == 'C':
		num_C += 1
	if dna[i] == 'G':
		num_G += 1
	if dna[i] == 'T':
		num_T += 1

print num_A, num_C, num_G, num_T
