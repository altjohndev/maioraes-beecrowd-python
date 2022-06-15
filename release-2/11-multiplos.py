valor = input().split()

a = int(valor[0])
b = int(valor[1])

if a == b:
    print("Sao Multiplos")
if a > b:
    if (a % b) == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
if b > a:
    if (b % a) == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
