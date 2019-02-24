x = int(input())
lista = [[], [], []]

for i in range(3):
    lista[i] = x % 60
    x = x // 60

print('%i:%i:%i' % (lista[2], lista[1], lista[0]))
