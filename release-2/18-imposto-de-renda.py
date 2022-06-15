salario = float(input())

if salario >= 0.00 and salario <= 2000.00:
  print('Isento')

if salario >= 2000.01 and salario <= 3000.00:
  imposto = salario - 2000
  imposto = (imposto / 100) * 8
  print(f'R$ {imposto:.2f}')

if salario >= 3000.01 and salario <= 4500.00:
  imposto = salario - 3000
  imposto = 79.9992 + ((imposto / 100) * 18)
  print(f'R$ {imposto:.2f}')

if salario > 4500:
  imposto = salario - 4500.00
  imposto = 79.9992 + 269.9982 + ((imposto / 100) * 28)
  print(f'R$ {imposto:.2f}')
