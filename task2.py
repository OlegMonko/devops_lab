import collections

print ('Enter size of list:')
n = int(input())
print ('Enter elements of list:')
l = list(map(int, input().split()))

c = collections.Counter()
for i in l:
    c[i]+=1
x,t=c.most_common()[0] #thank you for your advice
print(x)

