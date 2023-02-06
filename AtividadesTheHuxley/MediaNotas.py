numero = int(input())
contador = 0
soma = 0

while contador < numero :
    nota = int(input())
    soma += nota
    contador += 1

media = soma / numero

print(round(media, 1))
