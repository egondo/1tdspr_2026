def aumento(valor, percentual):
    novo_valor = (1 + percentual/100) * valor
    return novo_valor

valor = aumento(800, 80)

arq = open("pensao.txt", mode="w")
arq.write(str(valor))
arq.close()
