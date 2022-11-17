# Exemplo 1
"""
nome = input('Qual seu nome? ')
print('Ola {:=^20}!'.format(nome))
"""

# Exemplo 2
n1 = int(input('Um Valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 + n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('Soma {}, Multiplicação {}, Divisão {}'.format(s, m, d))
print('Div Inteira {}, Potência {}'.format(di, e))