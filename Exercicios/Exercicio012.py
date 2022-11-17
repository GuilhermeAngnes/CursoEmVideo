"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, em 5% de desconto.
"""

preço = float(input('Informe o Preço do produto: R$ '))

novo = preço - (preço * 5 / 100)

result = ('O produto com o valor de R$ {}, na promoção com o desconto de 5% vai custar R$ {}'.format(preço, novo))

print(result)
