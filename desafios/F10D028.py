#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

print('Estou pensando em um número...')
numero = random.randint(0, 5)

numero_usuario = int(input('Tente adivinhar o número que estou pensando: '))
if numero_usuario == numero:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou! O número que eu pensei foi {}'.format(numero))