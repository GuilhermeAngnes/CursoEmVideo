"""
O mesmo professor do desafio 19 quer sortear a ordem da apresentação  de trabalhos dos alunos.
Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle

al1 = str(input('Nome do 1º Aluno: '))
al2 = str(input('Nome do 2º Aluno: '))
al3 = str(input('Nome do 3º Aluno: '))
al4 = str(input('Nome do 4º Aluno: '))

lista = [al1, al2, al3, al4]

shuffle(lista)

print('Ordem de apresentação')
print(lista)
