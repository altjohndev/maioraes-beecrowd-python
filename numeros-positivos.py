positivos = 0

for numero in range(6):
    if float(input()) > 0:
        positivos += 1

print(f"{positivos} valores positivos")
