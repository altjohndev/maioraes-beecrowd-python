import math

line = input().split()
x1 = float(line[0])
y1 = float(line[1])

line = input().split()
x2 = float(line[0])
y2 = float(line[1])

# MATH é um módulo que fornece acesso às funções matemáticas
# MODULO é um arquivo contendo definições e comandosque
# que fazem parte da biblioteca padrão
# para serem usados em programas

calculo = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# SQRT pertence ao módulo math, e esta é a forma
# mais recomendada para realizar o cálculo de uma
# raiz quadrada em Python

print(f"{calculo:.4f}")
