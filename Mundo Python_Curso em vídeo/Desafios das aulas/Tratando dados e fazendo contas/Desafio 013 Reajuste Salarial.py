salario = float(input('Qual é o seu salário atual? R$ : '))
novoSalario = salario + (salario * 15 / 100)

print('O seu salário com 15% de aumento será R$:{:.2f}'.format(novoSalario))