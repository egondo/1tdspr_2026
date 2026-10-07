
#1  1   2   3   5   8   13  21  34

n = int(input("Digite n: "))
contador = 1

ant = 1
atual = 1

while contador < n:
    prox = atual + ant
    ant = atual
    atual = prox
    contador = contador + 1

print(f"O F_{n} é igual a {ant}")

#prox = atual + ant
#ant = atual
#atual = prox

#prox = atual + ant
#ant = atual
#atual = prox