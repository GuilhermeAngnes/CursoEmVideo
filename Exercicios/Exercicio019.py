"""
Um professor quer sortear um dos seus quatro alunos para apapar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.
"""
import random

aluno1 = str(input('Primeiro Aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Aluno: '))

# Lista em Python sempre fica dentro do conchetes;
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

escolher_aluno = random.choice(lista_alunos)

print('O Aluno escolhido foi {}'.format(escolher_aluno))
