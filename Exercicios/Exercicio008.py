"""
Escrever um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros
"""
medida = float(input('Informe uma Distancia em Metros: '))
cm = medida*100
mm = medida*1000

print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida,cm,mm))