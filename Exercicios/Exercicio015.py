"""
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
"""
dias = int(input('Quantos dias Alugados? '))
km = int(input('Quantos Km rodados? '))

pago = (dias * 60) + (km * 0.15)

result = 'O total a pagar é de R${:.2f}'.format(pago)

print(result)
