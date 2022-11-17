"""
Crie um programa que leia um numero Real e mostre em tela a sua porção inteira. 
"""
from math import trunc

num = float(input('Digite um numero: '))

result = ('O valor digitado é {} e sua porção inteira é {}' .format(num, trunc(num)))

print(result)
