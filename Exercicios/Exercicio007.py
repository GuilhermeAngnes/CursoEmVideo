"""
Desenvolva um programa que leia as duas notas de um aluno,
Calcule e mostre sua média
"""

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2)/2

print('A média ente {:.1f} e {:.1f} é igual a {:.2f}'.format(n1, n2, m))
