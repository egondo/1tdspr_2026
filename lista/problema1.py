n = int(input("Digite a qtd de alunos: "))

soma = 0
i = 0
conj = []
while i < n:
    nota = float(input("Digite a nota: "))
    soma = soma + nota
    conj.append(nota)
    i = i + 1

media = soma / n
acima = 0
abaixo = 0
for nota in conj:
    if nota <= media:
        abaixo = abaixo + 1
    else:
        acima = acima + 1

print(f"A média da turma foi {media}")
print(f"{abaixo} alunos foram abaixo da média")
print(f"{acima} alunos foram acima da média")