#entrada do problema:

salario_anterior = float(input("Salário anterior: "))
salario_atual = float(input("Salário atual: "))

diferenca = salario_atual - salario_anterior
percentual = (diferenca / salario_anterior) * 100

print("O percentual de aumento é " + str(percentual) + "%")