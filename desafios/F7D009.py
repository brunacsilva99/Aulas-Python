#Faça  um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
num = int(input('Digite um número inteiro: '))
print('A tabuada do número {} é: '.format(num))
for i in range(11):
    print('{} x {} = {}'.format(num, i, num * i))