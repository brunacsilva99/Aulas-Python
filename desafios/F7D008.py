#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros

medM = float(input('Digite a medida em metros: '))
medCM = medM * 100
medMM = medM * 1000
print('A medida de {} m é igual a {} cm e a {} mm'.format(medM, medCM, medMM))