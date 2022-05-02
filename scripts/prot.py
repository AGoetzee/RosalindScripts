'''
@author: Arthur Goetzee
@date: 02-05-22
@description: Translating RNA into Protein
http://rosalind.info/problems/prot/ 
'''

# Construct codon table dict
codon_table = {}
with open('data/codon_table.txt','r') as f:
    for line in f.readlines():
        line = line.split()
        for i in range(1,len(line)+1,2):
            codon_table[line[i-1]] = line[i]

# Get sequence and split into 3mers
with open('data/rosalind_prot.txt','r') as f:
    seq = f.readline()
    codons = [seq[i:i+3] for i in range(0,len(seq),3)]

# Translate codons to amino acids
prot = ''
for codon in codons:
    if codon_table[codon] == 'Stop':
        break
    else:
        prot += codon_table[codon]
    
with open('output/rosalind_prot_out.txt','w') as f:
    f.write(prot)