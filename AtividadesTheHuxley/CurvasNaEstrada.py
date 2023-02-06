c = 0
ce = 0
ci = 0
x = 0
y = 0
z = 0
contador = 0
total = 0
while True:
   
    entrada = str(input().lower())

    if entrada == "*":

        break

    else:
       
        if entrada == 'd' or entrada == 'dir' or entrada == 'direita':
            c += 1
            y = int(c)
        #else:

        if entrada == 'e' or entrada ==  'esq' or entrada == 'esquerda':
            ce += 1
            x = int(ce)

    contador+= 1
    w = contador    

       
    total = x + y
    incorreta = w - total   

print('Esquerda:', x)
print('Direita:', y)
print('Incorretas:', incorreta)