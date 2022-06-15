p1 = (input())
p2 = (input())
p3 = (input())

p4 = None

if p1 == 'vertebrado' and p2 == 'ave' and p3 == 'carnivoro':
  p4 = 'aguia'
elif p1 == 'vertebrado' and p2 == 'ave' and p3 == 'onivoro':
  p4 = 'pomba'
elif p1 == 'vertebrado' and p2 == 'mamifero' and p3 == 'onivoro':
  p4 = 'homem'
elif p1 == 'vertebrado' and p2 == 'mamifero' and p3 == 'herbivoro':
  p4 = 'vaca'
elif p1 == 'invertebrado' and p2 == 'inseto' and p3 == 'hematofago':
  p4 = 'pulga'
elif p1 == 'invertebrado' and p2 == 'inseto' and p3 == 'herbivoro':
  p4 = 'lagarta'
elif p1 == 'invertebrado' and p2 == 'anelideo' and p3 == 'hematofago':
  p4 = 'sanguessuga'
elif p1 == 'invertebrado' and p2 == 'anelideo' and p3 == 'onivoro':
  p4 = 'minhoca'
print(p4)
