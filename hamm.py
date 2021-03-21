'''
@author: Arthur Goetzee
@date: 21-03-21
@description: Counting Point Mutations from two strings of equal length.
http://rosalind.info/problems/hamm/ 
'''

INFILE = open('data/rosalind_hamm.txt', 'r')
OUTFILE = open('output/rosalind_hamm_sol.txt', 'w')

sequences = INFILE.readlines()
sequence_length = len(sequences[1])

hamm = 0
for nt in range(sequence_length):
    if sequences[0][nt] != sequences[1][nt]:
        hamm += 1

OUTFILE.write(str(hamm))

INFILE.close()
OUTFILE.close()