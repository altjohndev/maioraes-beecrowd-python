capital = int(input())

print(f'{capital}')

cem = int(capital // 100)
capital = capital % 100

cinquenta = int(capital // 50)
capital = capital % 50

vinte = int(capital // 20)
capital = capital % 20

dez = int(capital // 10)
capital = capital % 10

cinco = int(capital // 5)
capital = capital % 5

dois = int(capital // 2)
capital = capital % 2

um = int(capital // 1)
capital = capital % 1

print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')
