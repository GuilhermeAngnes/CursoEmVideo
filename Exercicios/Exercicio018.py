"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do Seno, Cosseno e Tangente desse ângulo
"""
import math

angulo = float(input('Informe um ângulo qualquer: '))
seno = math.sin(math.radians(angulo))
print('O Angulo {} tem o SENO de {:.2f}'.format(angulo, seno))


cosseno = math.cos(math.radians(angulo))
result_cosseno = ('O angulo {} tem COSSENO {:.2f}'.format(angulo, cosseno))
print(result_cosseno)

tangente = math.tan(math.radians(angulo))
result_tange = ('O angulo {} tem TANGENTE {:.2f}'.format(angulo, tangente))
print(result_tange)