#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada
num = float(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O número digitado é o {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(num, dobro, triplo, raiz))