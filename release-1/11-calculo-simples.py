line = input().split()
a = int(line[0])
b = int(line[1])
c = float(line[2])

line = input().split()
d = int(line[0])
e = int(line[1])
f = float(line[2])

x = (b * c) + (e * f)

print(f'VALOR A PAGAR: R$ {x:.2f}')
