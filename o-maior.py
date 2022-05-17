line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])

x = (a + b + abs (a - b)) / 2
y = (x + c + abs (x - c)) / 2

print(f'{y:.0f} eh o maior')
