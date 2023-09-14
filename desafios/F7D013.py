#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: '))
aumentado = salario * 1.15
print('Com 15% de aumento você receberá R${:.2f}'.format(aumentado))