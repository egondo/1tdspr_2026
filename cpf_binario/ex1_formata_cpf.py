cpf = int(input("CPF: "))
dc = cpf % 100
cpf = cpf // 100

parte3 = cpf % 1000
cpf = cpf // 1000

parte2 = cpf % 1000
cpf = cpf // 1000

print(f"{cpf}.{parte2}.{parte3}-{dc}")