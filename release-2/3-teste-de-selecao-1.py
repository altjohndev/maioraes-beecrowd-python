line = input().split()

a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])

aceito = b > c
aceito = aceito and d > a
aceito = aceito and (c + d) > (a + b)
aceito = aceito and d > 0
aceito = aceito and (a % 2) == 0

if aceito:
  print('Valores aceitos')
else:
  print('Valores nao aceitos')


# b>c d>a c+d>a+b c d positivos a par

# if b > c
# if b < c


# operações
# == igual
# != diferente
# > maior
# >= maior ou igual
# < menor
# <= menor ou igual
# and e
# or ou
# not não

# valores booleanos
# True
# False

# or
# 0 0 | 0
# 0 1 | 1
# 1 0 | 1
# 1 1 | 1

# and
# 0 0 | 0
# 0 1 | 0
# 1 0 | 0
# 1 1 | 1

# not
# 0 | 1
# 1 | 0

# if <True | False>:
#   <bloco do if>
# elif <True | False>:
#   <bloco do elif>
# elif <True | False>:
#   <bloco do elif>
# else:
#   <bloco do else>

# a = 1
# b = 2
# c = 3
# d = 4

# if a == 1:
#   print('P')
# elif b == 2:
#   print('Q')
# elif c == 3:
#   print('R')
# else:
#   print('S')

# a = 1
# b = 2
# c = 3
# d = 4

# if a == 1:
#   print('P')

# if b == 2:
#   print('Q')

# if c == 3:
#   print('R')
# else:
#   print('S')
