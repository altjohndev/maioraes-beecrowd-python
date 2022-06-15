nota = input().split()

n1 = float(nota[0])
n2 = float(nota[1])
n3 = float(nota[2])
n4 = float(nota[3])

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print(f"Media: {media:.1f}")

if media < 5:
    print("Aluno reprovado.")
elif media >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno em exame.")

    ne = float(input())

    print(f"Nota do exame: {ne:.1f}")

    mf = (media + ne) / 2

    if mf >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {mf:.1f}")
