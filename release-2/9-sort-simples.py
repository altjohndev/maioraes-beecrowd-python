numero = input().split()

n1 = int(numero[0])
n2 = int(numero[1])
n3 = int(numero[2])

maior = None
meio = None
menor = None

if n1 > n2:
  if n2 > n3:
    maior = n1
    meio = n2
    menor = n3
  else:
    menor = n2
    if n1 > n3:
      maior = n1
      meio = n3
    else:
      maior = n3
      meio = n1
else:
  if n2 > n3:
    maior = n2
    if n1 > n3:
      meio = n1
      menor = n3
    else:
      meio = n3
      menor = n1
  else:
    maior = n3
    meio = n2
    menor = n1

print(menor)
print(meio)
print(maior)
print('')
print(n1)
print(n2)
print(n3)
