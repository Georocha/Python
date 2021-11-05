'''co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa vai medir {}'.format(hi))'''
'''Acima a parte mais matematicamente escrita'''

import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa è {:.2f}'.format(hi))
