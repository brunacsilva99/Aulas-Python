#Faça um programa que leia um ângulo qualquer e mostre
# na te la o valor do seno, cosseno e tangente desse ângulo

import math
num = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O valor do seno de {} é igual {:.2}, o cosseno é {:.2} e a tangente é {:.2}'.format(num, sen, cos, tan))