## str = string;
## float = numero com ponto ou virgula;
## int = numero inteiro;
## bool = true ou false;
"""
# Variaveis;
n1 = int(input('Digite um valor maior que zero: '))
n2 = int(input('Digite outro valor maior que zero: '))

#Soma dos numeros;
s = n1 + n2

#Duas formas de mostrar o Resultado;
#print('A soma é: {}'.format(s))
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
"""

# Teste para saber se campo digitado
n = input('Digite algo: ')

# Verifica se campo é Numerico
#print(n.isnumeric())

# Verifica se campo é Letra
#print(n.isalpha())

# Verifica se todas Letras são Maiúsculas
print(n.isupper())