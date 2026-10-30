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

def busca(lista: list, titulo: str):
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
            lista[pos] = tit

        gen = input(f"Gênero ({lista[pos + 1]}): ")
        if gen:
            lista[pos + 1] = gen

        nota = input(f"Nota ({lista[pos + 2]}): ")
        if nota:
            lista[pos + 2] = float(nota)

        elenco = input(f"Elenco ({lista[pos + 3]}): ")
        if elenco:
            lista[pos + 3] = elenco
        
        ano = input(f"Ano ({lista[pos + 4]}): ")
        if ano:
            lista[pos + 4] = int(ano)

        classif = input(f"Classificação ({lista[pos + 5]}): ")
        if classif:
            lista[pos + 5] = classif
    

def consulta_titulo(lista: list) -> list:
    tit = input("Fragmento do título: ")
    i = 0
    resp = []
    while i < len(lista):
        titulo = lista[i]
        if tit.lower() in titulo.lower():
            resp.append(titulo)
            resp.append(lista[i + 3])
            resp.append(lista[i + 2])
        i = i + 6
    return resp

def imprime(lista: list):
    i = 0
    while i < len(lista):
        print(f"{i+1}) {lista[i]} - {lista[i+1]}: {lista[i+2]}")
        i = i + 3
        
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

        resultado = consulta_titulo(dados)
        imprime(resultado)

    elif op == 4:
        
        resultado = consulta_genero(dados)
        imprime(resultado)

    elif op == 5:
        apaga(dados)
    elif op == 6:
        print("Vá com Deus!")
    else:
        print("Opcao invalida")
