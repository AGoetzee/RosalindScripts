'''
@author: Arthur Goetzee
@date: 21-03-21
@description: Complementing a Strand of DNA from a string
http://rosalind.info/problems/revc/
'''

INFILE = open('data/rosalind_revc.txt', 'r')
OUTFILE = open('output/rosalind_revc_sol.txt', 'w')

seq = INFILE.read()
complement = ''

for nt in seq:
    if nt == 'A':
        complement += 'T'
    elif nt == 'C':
        complement += 'G' 
    elif nt == 'G':
        complement += 'C'
    elif nt == 'T':
        complement += 'A'

OUTFILE.write(complement[::-1])

INFILE.close()
OUTFILE.close()
