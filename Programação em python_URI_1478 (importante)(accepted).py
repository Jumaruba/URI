def primeira_metade(numero, matriz):
    for linha in range(numero):
        contador = 1
        for coluna in range(linha, numero):
            matriz[linha][coluna] = contador
            contador += 1
    return matriz


def metade_abaixo(numero, matriz):
    for coluna in range(numero - 1):
        contador = 2
        for linha in range(coluna + 1, numero):
            matriz[linha][coluna] = contador
            contador += 1
    return matriz


numero = int(input())

while numero != 0:
    if numero == 1:
        print(' ', 1)
    else:
        lista = [[0 for i in range(numero)] for j in range(numero)]
        lista = primeira_metade(numero, lista)
        lista = metade_abaixo(numero, lista)
        for j in range(numero):
            for k in range(numero - 1):
                print('{:>3}'.format(lista[j][k]), end=' ')
            print('{:>3}'.format(lista[j][numero - 1]))
    print()
    numero = int(input())
