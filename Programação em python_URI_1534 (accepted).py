x = int(input())

while True:
    try:
        matriz = [[0 for i in range(x)] for j in range(x)]

        for linha in range(x):
            for coluna in range(x):
                if linha + coluna == x - 1:
                    matriz[linha][coluna] = 2
                elif linha == coluna:
                    matriz[linha][coluna] = 1
                else:
                    matriz[linha][coluna] = 3

        for k in range(x):
            for l in range(x - 1):
                print(matriz[k][l], end='')
            print(matriz[k][x - 1])

        x = int(input())
    except EOFError:
        break
