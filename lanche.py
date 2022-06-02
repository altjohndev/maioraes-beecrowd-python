linha = input().split()

a = int(linha[0])
b = int(linha[1])

if a == 1:
  x = 4 * b
  print(f'Total: R$ {x:.2f}')
elif a == 2:
  x = 4.5 * b
  print(f'Total: R$ {x:.2f}')
elif a == 3:
  x = 5 * b
  print(f'Total: R$ {x:.2f}')
elif a == 4:
  x = 2 * b
  print(f'Total: R$ {x:.2f}')
elif a == 5:
  x = 1.5 * b
  print(f'Total: R$ {x:.2f}')
