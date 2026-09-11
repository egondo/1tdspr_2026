numero = int(input("RM: "))
=soma = 0

digito = numero % 100
soma = soma + digito
numero = numero // 10

digito = numero % 100
soma = soma + digito
numero = numero // 10

digito = numero % 100
soma = soma + digito
numero = numero // 10

digito = numero % 100
soma = soma + digito
numero = numero // 10

digito = numero % 100
soma = soma + digito
numero = numero // 10

print("A soma vale", soma)