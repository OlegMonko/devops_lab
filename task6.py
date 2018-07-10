dic = 'abcdefghijklmnopqrstuvwxyz '

f = open('INPUT.TXT', 'r')
s = f.read()
f.close()

result = ''
for i in range(len(s)-1):
    ind = int(s[i], 27) - i - 2
    result += dic[ind]

f = open('OUTPUT.TXT', 'w')
f.write(result)
f.close()
