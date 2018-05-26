def colunas(matriz, x, soma):
    for coluna in range(x):
        soma_agora = 0
        for linha in range(x):
            soma_agora += matriz[linha][coluna]
        if soma_agora != soma:
            return False  # soma_bool e -1

    return True


def diagonal_direita(matriz,x ,soma):
    soma_agora = 0
    for i in range(x):
        soma_agora+= matriz[i][i]
    if soma_agora != soma:
        return False  # soma_bool e -1
    return True

def diagonal_esquerda(matriz, x, soma):
    soma_agora= 0
    for i in range(x):
        soma_agora+= matriz[i][-i-1]
    if soma_agora!=soma:
        return False # soma_bool e -1
    return True

x = int(input())
matriz = []
soma_bool = True
continuar = True
for i in range(x):
    lista = list(map(int,input().split()))
    if continuar:
        soma = sum(lista)
        continuar = False
    if not continuar and (sum(lista)!= soma):
        soma_bool = False
    matriz.append(lista)
    lista = []

if soma_bool:
    soma_bool = colunas(matriz,x,soma)
    if soma_bool:
        soma_bool = diagonal_direita(matriz,x,soma)
        if soma_bool:
            soma_bool= diagonal_esquerda(matriz, x, soma)
            if soma_bool:
                print(soma)
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(-1)
else:
    print(-1)
