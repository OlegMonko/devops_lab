print('Enter x:')
x = int(input())
print('Enter y:')
y = int(input())
print('Enter z:')
z = int(input())
print('Enter N:')
N = int(input())

<<<<<<< HEAD
result = [[i, j, k]
          for i in range(x + 1) for j in range(y + 1)
          for k in range(z + 1) if i + j + k != N]
=======
result = list()
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != N:
                result.append([i, j, k])
>>>>>>> ec21db19cb33d501d104e8c87d9215b6ab295d14
print(result)
