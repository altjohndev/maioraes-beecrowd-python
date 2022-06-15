capital = int(input())

print(f"{capital}")

cem = capital // 100
capital = capital % 100
# // representa divisão de numero inteiro
# % representa o resto da divisão

cinquenta = capital // 50
capital = capital % 50

vinte = capital // 20
capital = capital % 20

dez = capital // 10
capital = capital % 10

cinco = capital // 5
capital = capital % 5

dois = capital // 2
um = capital % 2

print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")
