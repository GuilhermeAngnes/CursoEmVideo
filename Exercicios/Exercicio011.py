"""
Faça um programa que leia a largura e a altura de uma parede em metros.
Calcule a sua área e a quantidade de tinta necessária para pintá-la.
Sabendo que cada litro de tinta, pinta uma área de 2m².
"""
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg*alt
print('Dimensão {} x {} e sua Área é {}m² '.format(larg, alt, area))
tinta = area/2
print('{} Litros de Tinta '.format(tinta))
