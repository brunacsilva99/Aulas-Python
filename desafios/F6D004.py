#Faça um programa que leia algo pelo
#teclado e mostre na tela o seu tipo
#primitivo e todas as informações
#possíveis sobre ele.

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está em maisculas? {}'.format(algo.isupper()))
print('Está em minúsculas? {}'.format(algo.islower()))
print('Estpa capitalizada? {}'.format(algo.istitle()))
#esses comandos usados para saber caracteristicas da variavel são métodos dos
#objetos string.


