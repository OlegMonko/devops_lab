import collections

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
