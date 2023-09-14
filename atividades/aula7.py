#Usando o + para concatenar:
print('Oi'+'Olá')

#Usando o * para repetição de palavras:
print('Oi'*5)
print('='*20)

#################################################################################

#Tentando melhorar o print com operatores aritméticos:

#Modo padrão
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

#Ocupando um espaço pré-determinado:
#No caso 20 espaços de caractere
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))

#Alinhamento em um espaço pré-determinado:
#No caso 20 espaços de caractere

#Alinhamento a direita:
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))

#Alinhamento a esquerda:
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome))

#Alinhamento central:
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))

#Alinhamento em um espaço pré-determinado ocupando espaços em  branco com =:
#No caso 20 espaços de caractere
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

#############################################################################

#Explorando as operações aritméticas
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#o :.3f especifica que o resultado deve ser um float com 3 casas decimais
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira igual à {} e potência igual a {}'.format(di, e))