'''
@author: Arthur Goetzee
@date: 22-03-21
@description: Dictionaries.
http://rosalind.info/problems/ini6/ 
'''

INFILE = open('./data/rosalind_ini6.txt', 'r')
OUTFILE = open('./output/rosalind_ini6_sol.txt', 'w')

data = INFILE.read() \
    .strip('\n') \
    .split(' ')

words = {}
for word in data:
    if word not in words.keys():
        words[word] = 1
    else:
        words[word] += 1

my_str = ''
for word in words.keys():
    my_str = str(word) + ' ' + str(words[word]) + '\n'
    OUTFILE.write(my_str)
    my_str = ''

INFILE.close()
OUTFILE.close()