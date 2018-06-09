def caso_u(lista, matriz):
    for l in range(lista[0], lista[2] + 1):
        for c in range(lista[1], lista[3] + 1):
            matriz[l][c] += lista[4]
    return matriz


def caso_a(lista, matriz):
    print(matriz[lista[0]][lista[1]])


quant = int(input())
matriz = [[0 for k in range(501)] for m in range(501)]
for i in range(quant):
    lista = list(input().split())
    if lista[0] == 'U':
        lista.pop(0)
        lista = [int(h) for h in lista]
        matriz = caso_u(lista, matriz)
    else:
        lista.pop(0)
        lista = [int(h) for h in lista]
        caso_a(lista, matriz)
