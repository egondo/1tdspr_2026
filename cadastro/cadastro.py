def menu():
    opcoes = ["inclui", "altera", "consulta por título", "consulta gênero", "apaga", "sair"]
    print("MENU")
    i = 0
    while i < len(opcoes):
        print(f"{i+1} - {opcoes[i]}")
        i = i + 1
    opcao = int(input("Escolha: "))
    return opcao


def inclui(lista: list):
    tit = input("Título: ")
    gen = input("Gênero: ")
    nota = float(input("Nota: "))
    elenco = input("Elenco: ")
    ano = int(input("Ano: "))
    classif = input("Classificacao: ")
    lista.append(tit)
    lista.append(gen)
    lista.append(nota)
    lista.append(elenco)
    lista.append(ano)
    lista.append(classif)

def busca(lista:list, titulo: str):
    i = 0
    while i < len(lista):
        if lista[i] == titulo:
            return i
        i = i + 6
    return -1

def altera(lista: list):
    tit = input("Informe o titulo: ")
    pos = busca(lista, tit)
    if pos == -1:
        print("Filme não encontrado!")
    else:
        print("Informe se for diferente ou dê um Enter!")
        tit = input(f"Título ({lista[pos]}): ")
        if tit:
            lista.insert(pos, tit)

        gen = input(f"Gênero ({lista[pos + 1]}): ")
        if gen:
            lista.insert(pos + 1, tit)

        nota = input(f"Nota ({lista[pos + 2]}): ")
        if nota:
            lista.insert(pos + 2, float(nota))



dados = []    
print("Cadastro de filmes: ")
op = 0
while op != 6:
    op = menu()
    if op == 1:
        inclui(dados)
    elif op == 2:
        altera(dados)
    elif op == 3:
        consulta_titulo(dados)
    elif op == 4:
        consulta_genero(dados)
    elif op == 5:
        apaga(dados)
    elif op == 6:
        print("Vá com Deus!")
    else:
        print("Opcao invalida")
