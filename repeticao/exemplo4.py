#Escreva um programa que dadas duas notas de 0
#a 10 calcula a m´edia aritm´etica entre elas.

nota = float(input("Nota: "))
while nota > 10 or nota < 0:
    print(f"{nota} inválida!")
    nota = float(input("Digite a nota novamente: "))

print(nota)