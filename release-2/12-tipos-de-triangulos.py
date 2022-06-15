valores = input().split()

n1 = float(valores[0])
n2 = float(valores[1])
n3 = float(valores[2])

a = 0
b = 0
c = 0

if n1 < n2:
    a = n2
    c = n1
else:
    a = n1
    c = n2

if a < n3:
    b = a
    a = n3
else:
    b = n3

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if (a**2) == ((b**2) + (c**2)):
        print("TRIANGULO RETANGULO")
    elif (a**2) > ((b**2) + (c**2)):
        print("TRIANGULO OBTUSANGULO")
    elif (a**2) < ((b**2) + (c**2)):
        print("TRIANGULO ACUTANGULO")

    if a == b and b == c:
        print("TRIANGULO EQUILATERO")

    if ((a == b) and (a != c)) or ((b == c) and (b != a)) or ((a == c) and (a != b)):
        print("TRIANGULO ISOSCELES")
