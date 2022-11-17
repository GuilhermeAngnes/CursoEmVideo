# Qestão: Faça um programa que leia o numero inteiro e que escreva na tela seu sucessor e seu antecessor;

# Variável
n1 = int(input('Digite um Número: '))
# Resultado
print('O numero informado foi {}, seu antecessor é {} e seu sucessor é {}'.format(
    n1, (n1-1), (n1+1)))
