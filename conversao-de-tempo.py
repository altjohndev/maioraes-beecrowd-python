segundos = int(input())

hora = int(segundos // 3600)
segundos = segundos % 3600

minutos = int(segundos // 60)
segundos = segundos % 60

segundos = int(segundos // 1)

print(f'{hora}:{minutos}:{segundos}')
