n = int(input())
if n >= 1 and n <= 1000:
    novaRa = ''
    for i in range(n):
        Ra = input()
        if Ra.startswith('RA'):
            if len(Ra)>=20: 
                novaRa = Ra[2:]
                print(int(novaRa))
            else:
                print('INVALID DATA')
        else:
            print('INVALID DATA')
            
else:
    print('INVALID DATA')