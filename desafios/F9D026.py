#Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ')
print('A letra "A" aparece {} vezes'.format(frase.upper().count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.upper().find('A')))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.upper().rfind('A')))