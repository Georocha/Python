def contaVogais(palavra):
    vogais = 'aeiouAEIOU'
    totalvogais = 0

    for letra in palavra:
        if letra in vogais:
            totalvogais += 1

    return totalvogais

total =[]
totalpalavra=0
novototal=0
media=0
somatotal=0
a =''
while True:

    txt = input().split()

    if 'FIM' in txt:
        break
    else:

        for posicao in range(len(txt)):

            total.append(contaVogais(txt[posicao]))

            somatotal = sum(total)

        
        totalpalavra = len(txt)
        novototal = novototal + totalpalavra
        media = somatotal / novototal

if somatotal >= 1:
    print(f'{media:.2f}')
else:
    print('texto vazio')