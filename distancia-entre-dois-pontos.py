line = input().split()
x1 = float(line[0])
y1 = float(line[1])

line = input().split()
x2 = float(line[0])
y2 = float(line[1])

import math

calculo = math.sqrt((x2 - x1) ** 2 + (y2 -y1) ** 2)

print(f'{calculo:.4f}')
