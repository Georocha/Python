c = 0
le = []

while c < 7:

    p = str(input().upper())
    le.append(p)
    c += 1
    
c = le.count('CINEMA')
b = le.count('BOLICHE')

if int(c) > int(b):
    print('CINEMA')
else:
    print('BOLICHE')
    