def is_primo(num: int) -> bool:
    if num <= 1:
        return False

    div = 2
    while num % div != 0:
        div = div + 1
    
    if num > div:
        return False
    else:
        return True


#programa principal
contador = 0
num = 2
while contador < 100:
    #if is_primo(num) == True:
    if is_primo(num):
        print(num)
        contador = contador + 1
    num = num + 1
