## Importa todos arquivos da Biblioteca Math ##
#import math

## Importa apenas arquivos específicos do Math ##
from math import sqrt, ceil

num = int(input('Digite um Numero: '))
raiz = sqrt(num)

result = ('A Raiz de {} é igual a {}'.format(num, ceil(raiz)))
print(result)
