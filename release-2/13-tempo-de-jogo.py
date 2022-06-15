tempo = input().split()

i = int(tempo[0])
f = int(tempo[1])

if i > f:
  t = ((24 - i) + f)
  print(f'O JOGO DUROU {t} HORA(S)')
elif i < f:
  t = (f - i)
  print(f'O JOGO DUROU {t} HORA(S)')
elif i == f:
  print('O JOGO DUROU 24 HORA(S)')
