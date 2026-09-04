#Entrada de dados e saída

#comando input permite que o usuario digite 
#informacoes no seu programa; sempre devolve uma string
aux = input("Digite um número: ")

#funcao int(<str>), converte, se possível, a string 
#em um número inteiro
num_a = int(aux)

aux = input("Digite um número: ")
num_b = int(aux)

aux = input("Digite um número: ")
num_c = int(aux)

aux = input("Digite um número: ")
num_d = int(aux)

aux = input("Digite um número: ")
num_e = int(aux)

#realiza a soma das variaveis que armazenam a entrada
#do meu problema, atribuindo na variavel soma
soma = num_a + num_b + num_c + num_d + num_e

#imprimo a minha f-string com o valor da soma
print(f"A soma dos valores vale {soma}")

#O símbolo (comando) =, representa a atribuição de 
#valores a uma variável