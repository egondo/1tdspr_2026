#Ideia é fazer uma calculadora com as operacoes basicas 
#da mantematica
num_a = float(input("Digite o 1 numero: "))
num_b = float(input("Digite o 2 numero: "))

op = input("Informe a operação (+-*/): ")

#flag (sinal)
fez_conta = True

if op == "+":
    resultado = num_a + num_b
elif op == "-":
    resultado = num_a - num_b
elif op == "*":
    resultado = num_a * num_b
elif op == "/":

    if num_b != 0:
        resultado = num_a / num_b
    else:
        print("Nao posso dividir por 0")
        fez_conta = False

else:
    print("Operador invalido!")
    fez_conta = False


if fez_conta == True:
    print(f"{num_a} {op} {num_b} = {resultado:.4f}")