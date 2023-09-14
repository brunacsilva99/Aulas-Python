n = float(input('Digite um valor: ')) #Transforma em float
print(n)
print(type(n))
n = bool(input('Digite um valor: ')) #Transforma em booleano
print(n) #No caso diz se tem algum dado ou não, ou seja se o valor não for 0 ele vai ser True
print(type(n))
n = int(input('Digite um valor: ')) #Transforma em inteiro
print(n)
print(type(n))
n = str(input('Digite um valor: ')) #Transforma em string
print(n)
print(type(n))
n = str(input('Digite um valor: ')) #É originalmente uma string
print(n)
print(type(n))
print('Pode ser transformado em númerico: ',n.isnumeric()) #Verifica se é possível converter para um tipo de variável númerico
print('É composto apenas por letras: ',n.isalpha()) #Verifica se é composto APENAS por letras
print('Está dentro do alfabeto alphanumérico (letras e números) : ',n.isalnum()) #Verifica se é alfanumérico, caracteres de letras e números
print('É composto apenas por letras maiúsculas: ',n.isupper()) #Verifica se está com todas as letras maiúsculas
#Existem muitos outros metodos n.is para testar os valores das variáveis.


