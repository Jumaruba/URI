x = int(input())
lista = list(map(int, input().split()))
a1 = 1 + (((2 * sum(lista) // x) + x - 1) // 2) - x
mov = 0
movimento = 0
soma = sum(lista)
for i in range(x):
    mov += lista[i] - a1 - i
    if lista[i] > a1 + i:
        movimento += lista[i] - i - a1
if mov != 0:
    print(-1)
else:
    print(movimento)
