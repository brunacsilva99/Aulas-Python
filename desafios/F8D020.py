#O mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.

import random
lista = []
for i in range(4):
    lista.append(input('Digite o nome do {}º aluno: '.format(i+1)))
seq = random.sample(lista,4)
print('A ordem de apresentação é: {}'.format(seq))
#Eu tbm posso usar o shuffle porém ele mistura na própria lista
print('Agora vamos usar o shuffle:')
print('Lista Original: '.format(lista))
random.shuffle(lista)
print('Lista alterada: '.format(lista))
