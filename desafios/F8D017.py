#Faça um programa que leia o comprimento de cateto oposto e
#do cateto adjacente de um triângulo retângulo, e calcule e
#mostre o comprimento da hipotenusa.

import math
catOp = float(input('Digite o cateto oposto: '))
catAd = float(input('Digite o cateto adjacente: '))
hip = math.hypot(catAd, catOp)
print('A hipotenusa do triângulo retângulo é igual a {:.2f}'.format(hip))