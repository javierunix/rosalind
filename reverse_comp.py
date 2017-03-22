# print the reverse complementary of a given dna sequence
def reverse_complement(dna):
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	return ''.join([complement[base] for base in dna[::-1]])

sample = "TGAAACCCCGAGTGTAAGATGGAGAGTTGGGGGACTAGTGGCACGCCTAGCGAATCCGGCTTACACCGTGGACGTCACTCTACGAAAGCGGTACGAAAGTTCCGGCATTGTAGTCCTTGATAAATCTCGTGGATGATCCGTGATGCAGGGTGCCCAGAAATAGATTGACCTCACTTCGGTGTCTTCAGGGGTCAGACCCTTCCGGTTAGCCGTACACGGTAGATTTACACCGCCGTGTTATGCTAGGACCAAGTCGAATTGGGACATACGGGTCGCAGGTGCTTTGAACATTGTCTGACCCTCTCGCTAGGCGAGGCCGGTACCCCAGCTCAATACATGTTAGACAGCACAGGTTAAACTGAAAGAAGAAGTTCCCACTAAGGTGCGCTGAACACAGACTAGCGTCCCCAGGTCGCGCCCTGTTGCGACTATTTTCAATCGGAAACCCACCCTCACACGTCGCTCGCGCGAACGAGTACGCAAAGCTGCTTTCGACCCTCCAGCAGTACCTGCCAGTTCCATCGCCCCAAGAGCGACAAAGGGGCGGCATAACCAGATAGGCATTTTGGTCCCTTCGATTCCAGCATAGGTCTTACAGGTACCGATGACACCGGCCGAGAACCCAGGTGCATTGCTTAAGGCCGAACAAATAAAGCTCACTGTCGTGCCTAGGCTGTTGGTCCAACATAGGTTTGCATAAAGGTTCCACCCCGGCCGGTGTCAGAAAGTAAACAAAATGTGTCCGTCCCCAGAATCACCCGGATAATCATAATTCCCTCGAAAAGAGGAAAGCCATTATTTAAGAAGAAGGTTGGGAGGCCAAGTGTATGCTTGCGGAAGAAATGGCCGTCTCATGATACCGTATTCAAATGTAGTAACAGATTGGCTTGTCCCCTACTACACAGCAGTAACAGAAGCGGCGGACGTTTCAAGCTGCCTCCGGGCCTTCTCGAGTAGGTAGACGGGTATCATCGCCCGGTAAAACTCATAACG"
print reverse_complement(sample)