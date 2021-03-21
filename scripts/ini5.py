'''
@author: Arthur Goetzee
@date: 10-08-20
@description: Working with Files.
http://rosalind.info/problems/ini5/
'''


def writer(f,o):
    filetext = f.readlines()
    for word in range(1,len(filetext),2):
        o.write(filetext[word])
    return

infile = open('rosalind_ini5.txt', 'r')
outfile = open('ini5-out.txt','w+')

writer(infile,outfile)