'''
@author: Arthur Goetzee
@date: 21-03-21
@description: Counting DNA nucleotides from a string
http://rosalind.info/problems/dna/ 
'''

import io

INFILE = open('data/rosalind_dna.txt', 'rt')
OUTFILE = open('output/rosalind_dna_sol.txt', 'w')

# Read sequence
seq = INFILE.read().replace(' ', '')
print('File loaded')

# Initialize nucleotide dict
nt_counts = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0}

# Add count for each nucleotide
print('Reading sequence...')
for nt in seq:
    if nt == 'A':
        nt_counts[nt] += 1
    elif nt == 'C':
        nt_counts[nt] += 1
    elif nt == 'G':
        nt_counts[nt] += 1
    elif nt == 'T':
        nt_counts[nt] += 1

# Write to output file
for count in nt_counts.values():
    count_str = str(count) + ' '
    OUTFILE.write(count_str)
print('Output file written.')

INFILE.close()
OUTFILE.close()

