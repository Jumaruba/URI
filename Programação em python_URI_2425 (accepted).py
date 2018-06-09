x, y = map(int, input().split())

caixas = [0 for j in range(x)]
total = 0

for i in range(y):
    entrada, tempo = map(int, input().split())
    espera = min(caixas) - entrada
    if espera > 20:
        total += 1
    index = caixas.index(min(caixas))
    if min(caixas) >= entrada:
        caixas[index] += tempo
    else:
        caixas[index] = tempo + entrada

print(total)
