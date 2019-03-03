x = int(input())
lista = []
for i in range(x):
    lista.append(int(input()))
for m in range(x):
    if m == 0:
        anterior = 0
    agora = lista[m]
    if m == x - 1:
        futuro = 0
    else:
        futuro = lista[m + 1]
    print(futuro+agora+anterior)
    anterior = agora

