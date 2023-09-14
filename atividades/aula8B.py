from math import sqrt, floor #Sem o import os métodos não funcionam
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

#ctrl + space dá sugestão de comandos

#Raiz arredontada pra baixo:
print('A raiz arredondada pra baixo é {}'.format(floor(raiz)))