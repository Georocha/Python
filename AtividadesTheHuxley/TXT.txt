while True:
    cpf = str(input())

    if cpf != 'FIM':
        l = cpf.replace("-", ".").split(".")

        def calcula_digito(l):

            g1 = int(max(l[0]))
            g2 = int(max(l[1]))
            g3 = int(max(l[2]))
            soma = (g1 , g2 ,g3)
            somaGrupo = sum(soma)
            digitoVerif = somaGrupo % 10

            return str(digitoVerif)

        if calcula_digito(l) == l[3]:
                print('VALIDO')
        else:
                print('INVALIDO')   
    else:    
        break
