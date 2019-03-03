x1, y1, x2, y2 = map(int, input().split())

cima = abs(x2-x1)
baixo = abs(y2-y1)

total = cima + baixo

print(total)