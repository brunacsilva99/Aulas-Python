#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.

print('Digite o comprimento de três retas: ')
a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))

if(a < (b + c) and b < (a + c) and c < (a + b)):
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')