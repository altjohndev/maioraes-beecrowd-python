salario = float(input())

if salario >= 0 and salario <= 400.00:
  ns = (((salario / 100 ) * 15) + salario)
  print(f'Novo salario: {ns:.2f}')
  r = (salario / 100 ) * 15
  print(f'Reajuste ganho: {r:.2f}')
  print('Em percentual: 15 %')

if salario >= 400.01 and salario <= 800.00:
  ns = (((salario / 100 ) * 12) + salario)
  print(f'Novo salario: {ns:.2f}')
  r = (salario / 100) * 12
  print(f'Reajuste ganho: {r:.2f}')
  print('Em percentual: 12 %')

if salario >= 800.01 and salario <= 1200.00:
  ns = (((salario / 100 ) * 10) + salario)
  print(f'Novo salario: {ns:.2f}')
  r = (salario / 100) * 10
  print(f'Reajuste ganho: {r:.2f}')
  print('Em percentual: 10 %')

if salario >= 1200.01 and salario <= 2000.00:
  ns = (((salario / 100 ) * 7) + salario)
  print(f'Novo salario: {ns:.2f}')
  r = (salario / 100) * 7
  print(f'Reajuste ganho: {r:.2f}')
  print('Em percentual: 7 %')

if salario > 2000.00:
  ns = (((salario / 100 ) * 4) + salario)
  print(f'Novo salario: {ns:.2f}')
  r = (salario / 100) * 4
  print(f'Reajuste ganho: {r:.2f}')
  print('Em percentual: 4 %')
