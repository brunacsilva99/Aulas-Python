#Faça um programa que leia um número inteiro e mostre na tela o seu sucessos e seu antecessor
num = int(input('Digite um número inteiro'))
ant = num - 1
suc = num + 1
print('O número escolhido é o {}, seu antecessor é o {} e seu sucessor é o {}'.format(num, ant, suc))