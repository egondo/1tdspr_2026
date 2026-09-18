saldo = float(input("Saldo: "))


print("1 para deposito")
print("2 para saque")
escolha = int(input("Opcao: "))

valor = float(input("Valor: "))

fez_operacao = True

if escolha == 1: 
    saldo = saldo + valor
elif escolha == 2:
    if valor <= saldo:
        saldo = saldo - valor
    else:
        fez_operacao = False
        print("Operacao nao realizada")
else:
    fez_operacao = False
    print("Opção invalida!")

if fez_operacao:
    print(f"Seu novo saldo e {saldo}!")