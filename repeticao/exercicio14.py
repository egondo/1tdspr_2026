num = int(input("Digite um número: "))
soma = 0
div = 1
while div < num:
    if num % div == 0:
        #print(div)
        soma = soma + div
    div = div + 1

if soma == num:
    print(f"{num} é perfeito")
else:
    print(f"{num} não é perfeito")
