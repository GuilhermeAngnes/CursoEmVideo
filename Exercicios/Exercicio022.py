"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
 - O nome com todas as letras maiúsculas e minúsculas;
 - Quantas letras ao todo (sem considerar espaços);
 - Quantas letras tem o primeiro nome;
"""

nome = str(input('Qual o seu nome? ')).strip()

print('Nome em Maiusculo é {}'.format(nome.upper()))
print('Nome em Minúsculo é {}'.format(nome.lower()))
print('Qtde de Letras {}'.format(len(nome)-nome.count(' ')))
print('Count primeiro nome {} '.format(nome.find(' ')))