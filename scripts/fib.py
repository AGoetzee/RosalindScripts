'''
@author: Arthur Goetzee
@date: 01-05-22
@description: Rabbits and Recurrence Relations
http://rosalind.info/problems/fib/ 
'''

with open('data/rosalind_fib.txt','r') as f:
    n,k = tuple(map(int,f.readline().split()))

def fib(n,k):
    seq = [1,1]
    for i in range(n):
        new = seq[-2] * k + seq[-1]
        seq.append(new)
    return seq[n-1]
with open('output/rosalind_fib_out.txt', 'w') as f:
    f.write(str(fib(n,k)))

