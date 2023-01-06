"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep

pc = randint(0,5) # Computador sorteia um numero entre os 5
print('-=-' * 20)
print('Adivinhe o numero de 0 a 5 que estou pensando')
print('-=-' * 20)
jogador = int(input('Em que número estou pensando? '))
print('PROCESSANDO....')
sleep(2)
if jogador == pc:
    print('Parabéns! Você acertou...')
else:
    print('Errou! Estava pensando no numero {}'.format(pc))
