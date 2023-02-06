e = input().split()

def aposentadoria(idade, tempo):
    idade = int(e[0])
    tempo = int(e[1])
    
    if idade < 60 and tempo >= 30:
        print('Pode se aposentar')
    #else:
    if idade < 60 and tempo < 30:
        t3 = 30 - tempo
        if t3 > 1:
            print('N�o pode se aposentar: Ainda faltam {} anos de trabalho'.format(t3))
        else:
            print('N�o pode se aposentar: Ainda falta {} ano de trabalho'.format(t3))

    if idade >= 60 and idade < 65:
        if tempo >= 25:
            print('Pode se aposentar')
        #else:
        if tempo < 25 and tempo > 5:
            t1 = 25 - tempo
            if t1 > 1:
                print('N�o pode se aposentar: Ainda faltam {} anos de trabalho'.format(t1))
            else:
                     print('N�o pode se aposentar: Ainda falta {} ano de trabalho'.format(t1)) 
        else:
            t4 = 5 - tempo
            if t4 > 1:
                print('N�o pode se aposentar: Ainda faltam {} anos de trabalho'.format(t4))
            else:
                print('N�o pode se aposentar: Ainda falta {} ano de trabalho'.format(t4))
                
    if idade >= 65 and tempo >= 5:
        print('Pode se aposentar')
    #else:
        if idade >= 65 and tempo < 5:
            t2 = 5 - tempo
            if t2 > 1:
                print('N�o pode se aposentar: Ainda faltam {} anos de trabalho'.format(t2)) 
            else:
                print('N�o pode se aposentar: Ainda falta {} ano de trabalho'.format(t2))
                    
aposentadoria(int(e[0]), int(e[1]))
