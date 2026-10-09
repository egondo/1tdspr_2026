#723.381.890-86
cpf9 = int(input("Digite o CPF com 9 digitos: "))

mult = 2
soma = 0

while cpf9 != 0:
    dig = cpf9 % 10
    #print(dig * mult)
    soma = soma + dig * mult
    cpf9 = cpf9 // 10
    mult = mult + 1

resto = soma % 11
if resto < 2:
    print("1 digito verificador vale 0")
else:
    print(f"1 digito verificador vale {11 - resto}")


#Questao: na repetição, o while terminou apenas quando cpf9 é zero, mas vou precisar dele para calcular o segundo digito verificador!