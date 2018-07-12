import collections

<<<<<<< HEAD
while True:
    n = int(input())
    if 1 <= n <= 100000:
        break

c = collections.Counter()
for i in range(n):
    c[input()] += 1

print(len(c))
result = ''
for i in c.values():
    result += str(i) + ' '
print(result[:-1])

=======
print('Enter the number of words')
n = int(input())

c = collections.Counter()
for i in range(n):
    print('Enter', i + 1, 'word')
    c[input()] += 1

print(len(c))
for i in c.values():
    print(i, end=' ')
>>>>>>> ec21db19cb33d501d104e8c87d9215b6ab295d14
