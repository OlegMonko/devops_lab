keyb = 'qwertyuiopasdfghjklzxcvbnm'
f = open ('INPUT.TXT', 'r')
i=keyb.find(f.read(1))
f.close()

f = open ('OUTPUT.TXT', 'w')
f.write(keyb[i+1])
f.close()