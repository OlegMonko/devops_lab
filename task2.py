import collections

print('Enter size of list:')
n = int(input())
print('Enter elements of list:')
ll = list(map(int, input().split()))

c = collections.Counter()
for i in ll:
    c[i] += 1
x, t = c.most_common()[0]  # thank you for your advice
print(x)
