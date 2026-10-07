cpf9 = int(input("Digite o CPF com 9 digitos: "))

mult = 2

dig = cpf9 % 10
print(dig * mult)
cpf9 = cpf9 // 10
mult = mult + 1

dig = cpf9 % 10
print(dig * mult)
cpf9 = cpf9 // 10

