def contaVogais(palavra):

    vogais = 'aeiouAEIOU'
    totalvogais = 0

    for letra in palavra:
        if letra in vogais:
            totalvogais += 1

    return totalvogais

listacons = []
maior = 1
a = ''
maiorPalavra = ''
totalvogais = 0
totalcons = 0
contevazio = 0


while True:

    txt = input().split()

    if 'FIM' in txt:
        break
    else:
        #else:
            if len(txt):
                contevazio += 1
                #a = 'V'   
                #pass
            for posicao in range(len(txt)):
                    
                    a = contaVogais(txt[posicao])
                    
                    #contaVogais(txt)
                    if a > 0:

                        if contaVogais(txt[posicao]) >= maior:
                            maior = contaVogais(txt[posicao])
                            maiorPalavra = txt[posicao]
                            totalvogais += 1

            for posicao in range(len(txt)):

                    #contaVogais(txt)
                    if a == 0:
                        listacons.append(txt[posicao])
                        ultimaPalavra = listacons[-1]
                        totalcons += 1

#if contevazio == 1 :
    #print('texto vazio')
#else:
if totalvogais != 0:
    print(maiorPalavra)
else:
    if totalcons != 0:
        print(ultimaPalavra)
    else:
        #if vazio(txt):
        print('texto vazio')