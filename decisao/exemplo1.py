idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
    print("Parabéns, vc pode tirar carta de motorista")
else:
    print("Você nao pode dirigir!")

print(f'A sua idade é {idade}')
print('A sua idade é', idade)
print('A sua idade é ' + str(idade))
print("Qual a diferença de falar 'por favor' e 'por obséquio'")