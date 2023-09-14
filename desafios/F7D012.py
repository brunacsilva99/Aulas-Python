#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço original: '))
precoDesconto = preco * 0.95
print('O preço fica igual à R${:.2f} com desconto de 5%'.format(precoDesconto))