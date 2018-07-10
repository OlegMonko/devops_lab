def verify(n):
    string_of_num = str(n)
    for j in string_of_num:
        if j == '0' or n % int(j) > 0:
            return False
    return True

print ('Enter: left = x, right = y')
pars = input().split()
left = int((pars[2]).rstrip(','))
right = int(pars[5])

result = []
for i in range (left, right+1):
    if verify (i):
        result.append(i)
print(result)

