#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
maior = n1
menor = n1
if(n2 > maior):
    maior = n2
if(n3 > maior):
    maior = n3
if(n2 < menor):
    menor = n2
if(n3 < menor):
    menor = n3

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))