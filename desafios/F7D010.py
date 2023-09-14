#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considerando o dolar = R$3,27

dTotal = float(input('Quanto dinheiro você tem em reais? '))
qtdeDolar = dTotal//3.27
print('Com o total de R${:.2f} você pode comprar {} dolares'.format(dTotal, int(qtdeDolar)))