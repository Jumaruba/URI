portugues = list(map(int, input().split()))
portugues.pop(0)
matematica = list(map(int, input().split()))
matematica.pop(0)
fisica = list(map(int, input().split()))
fisica.pop(0)
quimica = list(map(int, input().split()))
quimica.pop(0)
biologia = list(map(int, input().split()))
biologia.pop(0)
quantidade = int(input())
conjuntos = []
soma = 0

for p in portugues:
    for m in matematica:
        for f in fisica:
            for q in quimica:
                for b in biologia:
                    conjuntos.append(p + m + f + q + b)
conjuntos.sort()
for i in range(1,quantidade+1):
    soma += conjuntos[-i]


print(soma)
