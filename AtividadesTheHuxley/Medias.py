numero = input().split()
contador = 0
soma = 0
somaMediaHarmonica = 0
nl = []
mediaGeometrica = 1

while contador < len(numero):

    soma += float(n[contador])
    mediaGeometrica *= float(n[contador])

    somaMediaHarmonica += (1 / float(n[contador]))
    mediaHarmonica = len(numero) / somaMediaHarmonica 
    
    contador +=1

mediaAritmetica = soma / len(numero)
mmg = mediaGeometrica ** (1/5)

print(f'{ma:.3f}'.format(mediaAritmetica))
print(f'{mh:.3f}'.format(mediaHarmonica))
print(f'{mmg:.3f}'.format(mmg))
