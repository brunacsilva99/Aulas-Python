#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: '))
if(salario > 1250):
    print('O salário com aumento é R${:.2f}'.format(salario * 1.1))
else:
    print('O salário com aumento é R${:.2f}'.format(salario * 1.15))