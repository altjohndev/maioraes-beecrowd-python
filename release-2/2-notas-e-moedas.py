# https://www.beecrowd.com.br/judge/pt/problems/view/1021

linha = input().split(".")

print("NOTAS:")

restante = int(linha[0])

print(f"{restante // 100} nota(s) de R$ 100.00")

restante %= 100
print(f"{restante // 50} nota(s) de R$ 50.00")

restante %= 50
print(f"{restante // 20} nota(s) de R$ 20.00")

restante %= 20
print(f"{restante // 10} nota(s) de R$ 10.00")

restante %= 10
print(f"{restante // 5} nota(s) de R$ 5.00")

restante %= 5
print(f"{restante // 2} nota(s) de R$ 2.00")

print("MOEDAS:")

print(f"{restante % 2} moeda(s) de R$ 1.00")

restante = int(linha[1])

print(f"{restante // 50} moeda(s) de R$ 0.50")

restante %= 50
print(f"{restante // 25} moeda(s) de R$ 0.25")

restante %= 25
print(f"{restante // 10} moeda(s) de R$ 0.10")

restante %= 10
print(f"{restante // 5} moeda(s) de R$ 0.05")

print(f"{restante % 5} moeda(s) de R$ 0.01")
