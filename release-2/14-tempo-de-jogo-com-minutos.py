tempo = input().split()

hi = int(tempo[0])
mi = int(tempo[1])
hf = int(tempo[2])
mf = int(tempo[3])

i = ((hi * 60) + mi)
f = ((hf * 60) + mf)

if i > f:
  t = ((1440 - i) + f)
  th = t // 60
  tm = t % 60
  print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
elif i < f:
  t = (f - i)
  th = t // 60
  tm = t % 60
  print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
elif i == f:
  print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
