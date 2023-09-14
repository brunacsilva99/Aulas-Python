#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
#Sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
area = larg * alt
Ltinta = area/2

print('A parede tem uma área de {:.2f}m² e será necessário {:.2f}L de tinta para pinta-la'.format(area, Ltinta))