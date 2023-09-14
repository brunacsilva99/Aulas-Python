#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o arro ficou alugado? '))
Km = float(input('Quantos foram os Km percorridos com o carro alugado? '))
valor = (dias * 60.00) + (Km * 0.15)
print('O valor a ser pago pelos {:.2f}Km percorridos e {} dias é de R${:.2f}'.format(Km, dias, valor))