"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
Considere US 1,00 = R$ 3,27
"""

real = float(input('Quanto dinheiro você tem? R$ '))
dolar = real / 5.32

print('$ {:.2f}'.format(dolar))
