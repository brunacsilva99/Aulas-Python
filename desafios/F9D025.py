#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite seu nome completo: ')
if('SILVA' in nome.upper()):
    print('Seu nome tem "Silva"')
else:
    print('Seu nome não tem "Silva"')