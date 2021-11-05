from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você desejar: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem \n o Seno de {:.2f} , o Cosseno de {:.2f} e a tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))