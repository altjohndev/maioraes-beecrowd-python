import math

valor = input().split()

a = float(valor[0])
b = float(valor[1])
c = float(valor[2])

if a != 0 and ((b ** 2) - (4 * a * c)) > 0:

  x1 = (- b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
  x2 = (- b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
  print(f'R1 = {x1:.5f}')
  print(f'R2 = {x2:.5f}')

else:
  print('Impossivel calcular')
