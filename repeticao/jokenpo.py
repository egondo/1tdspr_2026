import random

papel = '\u270B\uFE0F'
tesoura = '\u270C\uFE0F'
pedra = '\u270A\uFE0F'

msg = f'''1 {papel} 
2 {tesoura}
3 {pedra}'''
print(msg)
jogada = int(input("escolha: "))
print(jogada)

cpu = random.randint(1, 3)

if jogada == 1 and cpu == 2:
    print('CPU venceu!')
elif jogada == 2 and cpu == 3:
    print('CPU venceu!')
elif jogada == 3 and cpu == 1:
    print('CPU venceu!')
elif jogada != cpu:
    print('Humano venceu!')
else:
    print("Empate")

print(f"Hum {jogada} X {cpu} CPU")

print('\u270C\uFE0F')
print('\u270A\uFE0F')
print('\u270B\uFE0F')
