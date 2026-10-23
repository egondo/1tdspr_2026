def maior_menor(lista):
    max = lista[0]
    min = lista[1]

    for num in lista:
        if num < min:
            min = num
        if num > max:
            max = num

    return [min, max] #retornado uma lista