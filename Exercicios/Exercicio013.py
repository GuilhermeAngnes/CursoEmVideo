"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Informe o Salário do Funcionário: R$ '))
aumento = float(
    input('informe a Porcentagem de aumento que irá dar ao Funcionário: '))

novo = salario + (salario*aumento/100)

result = ('O salário atual é de R$ {:.2f}, com o aumento de {}%, o salário do funcionário será R$ {:.2.f}'.format(
    salario, aumento, novo))
print(result)
