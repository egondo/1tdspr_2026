import math

num = float(input("Digite um número: "))
if num < 0:
    print("Impossivel extrair raiz quadrada de numero negativo!")
    res = num ** 0.5
    print(res)
else:
    raiz = math.sqrt(num)
    print(f"A raiz quadrade de {num} e {raiz}")