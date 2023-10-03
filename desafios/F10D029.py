#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

valorMultaPorKm = 7
limiteVelocidade = 80
velocidade = float(input('Digite a velocidade do carro: '))
if(velocidade > limiteVelocidade):
    print('Você foi multado em R${:.2f}'.format((velocidade - limiteVelocidade) * valorMultaPorKm))