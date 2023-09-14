#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Digite uma temperatura em graus Celsius: '))
tempF = (temp*(9/5))+32
print('A temperatura de {}ºC é igual {}ºF'.format(temp, tempF))