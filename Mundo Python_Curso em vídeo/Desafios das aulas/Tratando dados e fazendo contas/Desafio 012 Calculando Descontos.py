preco = float(input('Qual é o preço do produto? R$ '))
desconto = int(input('Qual o desconto recebido? :'))
precoDesconto = preco - (preco * desconto / 100)

print('O produto com desconto de {} %  custará R${:.2f}'.format(desconto, precoDesconto))