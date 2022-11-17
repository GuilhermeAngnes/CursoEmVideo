"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
### MANEIRA TRADICIONAL ### 
"""
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

calc = (co ** 2 + ca ** 2) ** (1/2)

result = ('O comprimento da hipotenuas é {:.2f}' .format(calc))

print(result)
"""
### COM BIBLIOTECA PYTHON ###
import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

hipot = math.hypot(oposto, adjacente)

result = ('O comprimento da hipotenuas é {:.2f}' .format(hipot))

print(result)