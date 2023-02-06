alfa = 'abcdefghijklmnopqrstuvwxyz'
alfaM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
novaPosicao = 0
textoCriptografado =''
texto = input()

if len(texto) <= 100:

    for letra in texto:
        if letra.islower():
            posicao = alfa.find(letra)
            
            if posicao == -1:
                textoCriptografado += letra
            else:
                if n > 0:
                    novaPosicao = posicao + n
                   
                else:
                    novaPosicao = posicao + n
                
                novaPosicao = novaPosicao % len(alfa)
                textoCriptografado += alfa[novaPosicao:novaPosicao+1]
        else:

            posicao = alfaM.find(letra)
            
            if posicao == -1:
                textoCriptografado += letra
                
            else:
                if n > 0:
                    novaPosicao = posicao + n
                    
                else:
                    novaPosicao = posicao + n
                    
                novaPosicao = novaPosicao % len(alfaM)
                textoCriptografado += alfaM[novaPosicao:novaPosicao+1]

print(textoCriptografado)