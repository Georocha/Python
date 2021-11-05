##  Programa que pergunta a quantidade de KM percorridos por um carro alugado
#   e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#   sabendo que o carro custa R$ 60 por dia e R$ 0.15 por Km rodado.

dias = int(input("Quantos dias o carro ficou alugado? "))
km = float(input("Quantos Quilômetros rodados? "))
pagamento = (dias * 60) + (km * 0.15)

print("O total a pagar é de R${:.2F} ".format(pagamento))