idade = int(input())

ano = idade // 365
idade = idade % 365

mese = idade // 30
dia = idade % 30

print(f"{ano} ano(s)")
print(f"{mese} mes(es)")
print(f"{dia} dia(s)")
