'''
@author: Arthur Goetzee
@date: 30-05-22
@description: Computing GC Content
http://rosalind.info/problems/gc/ 
'''

INFILE = open('data/rosalind_gc.txt', 'rt')

seq_dict = {}
for line in INFILE.readlines():
    if line.startswith('>'):
        seq = ''
        id = 0000
        id = line[-5:].strip('\n')
    else:
        seq += line.strip('\n')
        seq_dict[id]=seq.strip('\n')
INFILE.close()

gc_dict = {}
for id in seq_dict.keys():
    gc_num = 0
    for nt in seq_dict[id]:
        if nt == 'G' or nt == 'C':
            gc_num += 1
    gc_content = (gc_num/len(seq_dict[id]))*100
    gc_dict[id] = gc_content

with open('output/rosalind_gc_out.txt', 'w') as OUTFILE:
    id = max(gc_dict,key=gc_dict.get)
    OUTFILE.write('Rosalind_%s\n%.6f\n' %(id,gc_dict[id]))
