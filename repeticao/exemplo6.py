num = int(input("Digite um num positivo: "))
while num <= 0:
    print("Numero invalido!")
    num = int(input("Digite um num positivo: "))

div = 1

while div <= num:
    if num % div == 0:
        print(div)
    div = div + 1



