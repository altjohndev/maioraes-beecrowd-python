numero = input().split()

n1 = int(numero[0])
n2 = int(numero[1])
n3 = int(numero[2])

cres = [n1, n2, n3]
cres.sort()
print('\n'.join(map(str, cres)))
print('')
print(n1)
print(n2)
print(n3)
