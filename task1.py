print('Enter x:')
x = int(input())
print('Enter y:')
y = int(input())
print('Enter z:')
z = int(input())
print('Enter N:')
N = int(input())

result = list()
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != N:
                result.append([i, j, k])
print(result)
