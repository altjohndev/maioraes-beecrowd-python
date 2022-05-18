line = input().split()
a = float(line[0])
b = float(line[1])
c = float(line[2])

area = (a * c) / 2
print(f'TRIANGULO: {area:.3f}')

area = 3.14159 * (c ** 2)
print(f'CIRCULO: {area:.3f}')

area = ((a + b) * c) / 2
print(f'TRAPEZIO: {area:.3f}')

area = b * b
print(f'QUADRADO: {area:.3f}')

area = a * b
print(f'RETANGULO: {area:.3f}')
