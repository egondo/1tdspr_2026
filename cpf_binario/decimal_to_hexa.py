### para transformar um decimal para binario, realizo uma sequencia de divisoes por 2

### para transformar um decimal para hexadecimal, o que eu faço?
### Resp: realizar uma sequencia de divisoes por 16

decimal = int(input("Decimal: "))
resp = ''

while decimal != 0:
    resto = decimal % 16
    decimal = decimal // 16
    if resto < 10:
        resp = str(resto) + resp
    elif resto == 10:
        resp = 'A' + resp
    elif resto == 11:
        resp = 'B' + resp
    elif resto == 12:
        resp = 'C' + resp
    elif resto == 13:
        resp = 'D' + resp
    elif resto == 14:
        resp = 'E' + resp
    elif resto == 15:
        resp = 'F' + resp

print(f"Hexadecimal é {resp}")