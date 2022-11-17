"""
Escreva um programa que converta uma tenmperatura digitada em ºC e converta para ºF.
"""
c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32

result = ('A temperatura de {} ºC corresponde a ºF é de {} ºF'.format(c, f))

print(result)
