import collections

print ('Enter the number of words')
n=int(input())

c = collections.Counter()
for i in range(n):
    print ('Enter', i+1, 'word')
    c[input()] += 1

print (len(c))
for i in c.values():
    print(i, end=' ')
