escolha = 0
while escolha != 6:
    print("1 - Jogo da Forca")
    print("2 - BlackJack")
    print("3 - Jogo de Números")
    print("4 - Jogo da Velha\n5 - Jokenpo")
    print("6 - Sair")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        print("Você vai jogar o Jogo da Forca")
    elif escolha == 2:
        print("Você vai jogar o BlackJack")
    elif escolha == 3:
        print("Você vai jogar o Jogo de Números")
    elif escolha == 4:
        print("Você vai jogar o Jogo da Velha")
    elif escolha == 5:
        print("Você vai jogar o Jokenpo")
    elif escolha == 6:
        print("Saindo do Menu de Jogos")
    else:
        print("Escolha inválida")

