reais = input().split()

n1 = float(reais[0])
n2 = float(reais[1])
n3 = float(reais[2])

p = n1 + n2 + n3
a = ((n1 + n2) * n3) / 2

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print(f"Perimetro = {p:.1f}")
else:
    print(f"Area = {a:.1f}")
