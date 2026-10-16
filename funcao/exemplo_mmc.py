def calcula_mmc(a: int, b: int) -> int:
    mmc = a
    while mmc % a != 0 or mmc % b != 0:
        mmc = mmc + a
    return mmc    

x = 6
y = 14
resultado = calcula_mmc(x, y)
print(f"O mmc({x}, {y}) é {resultado}")


#a = 6
#b = 14

#mmc = a
#while mmc % a != 0 or mmc % b != 0:
#    mmc = mmc + a

#print(f"O mmc vale {mmc}")
