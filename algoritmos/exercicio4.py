#Entrada de dados

aux = input("Digite o 1 número inteiro: ")
num1 = int(aux)

num2 = int(input("Digite o 2 número inteiro: "))

soma = num1 + num2
produto = num1 * num2

#divisao inteira
divisao = num1 // num2  

#resto da divisao
resto = num1 % num2

#saida do algoritmo
print(num1, '+', num2, '=', soma)
print(num1, '*', num2, '=', produto)
print(num1, '//', num2, '=', divisao)
print(num1, '%', num2, '=', resto)