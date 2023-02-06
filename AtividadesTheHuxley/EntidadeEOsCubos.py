n = int(input())
maxA = 0
somaN = 0
somaL = ''

if n == 1:
    print(1)
else:
    if n > 1 and n <= 4:
        print(1)
    else:

        for i in range(1, n + 1 ):

            somaN += (1 + i) * i
            somaL = (somaN / 2)

            if somaL <= n:
                maxA += 1
            else:
                break
       
        print(maxA)