'''
@author: Arthur Goetzee
@date: 21-03-21
@description: Transcribing DNA into RNA from a string
http://rosalind.info/problems/rna/ 
'''

INFILE = open('data/rosalind_rna.txt', 'r')
OUTFILE = open('output/rosalind_rna_sol.txt', 'w')

seq = INFILE.read().replace('T', 'U')

OUTFILE.write(seq)

INFILE.close()
OUTFILE.close()
