numero, mesa, limite = map(int, input().split())
lista = [0, 0]
for i in range(0, (numero - 1) // 2):
    x = int(input())
    if abs(x - mesa) <= limite:
        lista[0] += abs(x - mesa)
        mesa = x
    y = int(input())
    if abs(y - mesa) <= limite:
        lista[1] += abs(y - mesa)
        mesa = y

print(lista[0], lista[1])
