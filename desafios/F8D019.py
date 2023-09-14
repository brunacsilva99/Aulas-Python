#Um professor quer sortear um dos seus quatro alunos para apagar
# o quadro. Faça um programa que ajude ele, lendo o nome deles e
# escrevendo o nome do escolhido

import random
lista = []
for i in range(4):
    lista.append(input('Digite o nome do {}º aluno: '.format(i+1)))
name = random.choice(lista)
print('O aluno sorteado é o {}'.format(name))
