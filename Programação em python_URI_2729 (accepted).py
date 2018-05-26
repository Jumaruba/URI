quantidade = int(input())

for i in range(quantidade):
    x = list(input().split())
    quero = set(x)
    x = sorted(quero)
    for i in range(len(x)-1):
        print(x[i], end=' ')
    print(x[len(x)-1])

