soma = 0

num = int(input("Digite num: "))

while num != 0:
    if num % 2 == 0:
        soma = soma + num
    num = int(input("Digite um num: "))

print(f"A soma dos pares vale {soma}")



