def matriz_const(n):
    matriz = []
    for i in range(n):
        x = list(input())
        matriz.append(x)
    return matriz


def calculando(linha, coluna):
    comida = '.'
    if matriz[linha][coluna] == 'o':
        comida = True
    elif matriz[linha][coluna] == 'A':
        comida = False
    return comida


def caminhos(matriz):
    comida = 0
    lista_comida = []
    for linha in range(n):
        for coluna in range(n):
            if linha % 2 == 1:
                if matriz[linha][-1-coluna] == 'o':
                    comida +=1
                    lista_comida.append(comida)
                elif matriz[linha][-1-coluna] == 'A':
                    comida = 0
            else:
                if matriz[linha][coluna] == 'o':
                    comida +=1
                    lista_comida.append(comida)
                elif matriz[linha][coluna] == 'A':
                    comida = 0
    return lista_comida


n = int(input())

matriz = matriz_const(n)
lista_comida = caminhos(matriz)
print(max(lista_comida))
