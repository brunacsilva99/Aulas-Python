import math #Sem o import os métodos não funcionam
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,raiz))

#ctrl + space dá sugestão de comandos

#Raiz arredontada pra baixo:
print('A raiz arredondada pra baixo é {}'.format(math.floor(raiz)))


#Usando a biblioteca random

import random
#Gerador de número real(float) aleatório entre 0 e 1
A = random.random()
print('O número aleatório é: {}'.format(A))
#Pode ser usado o metódo randInt() para geral número inteiro
# entre um intervalo definido por você, no exemplo de 1 a 10
B= random.randint(1, 10)
print('O inteiro aleatório é: {}'.format(B))


#Usando biblioteca externa

import emoji
print(emoji.emojize("Olá, Mundo :sunglasses:", use_aliases=True))
print(emoji.emojize("Olá, Mundo :earth_americas:", use_aliases=True))