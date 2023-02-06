while True:
    ph = float(input())
    
    if ph < 7 and ph > 0:
        print('ACIDA')
    if ph > 7:
        print('BASICA')
    if ph  == 7:
        print('NEUTRA')
    if ph < 0:
        break
