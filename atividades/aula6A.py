n1 = input('Digite um valor: ')
print(type(n1)) #Para imprimir o tipo da variável

#A princípio a classe será str mas se adicionar o int() fica como int:
n1 = int(input('Digite um valor: '))
print(type(n1)) #Para imprimir o tipo da variável

#Depois da correção
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
s = n1 + n2
#print('A soma entre ',n1,' e ',n2,'vale ',s)
print('A soma entre {} e {} vale {}'.format(n1,n2,s))