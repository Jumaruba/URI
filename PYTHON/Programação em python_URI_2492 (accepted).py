def invertivel(numero):
    entrada = []
    saida = []
    for i in range(numero):
        n_entrada, separador, n_saida = str(input()).partition(' -> ')
        entrada.append(n_entrada)
        saida.append(n_saida)
    if len(set(entrada)) != len(entrada):
        print('Not a function.')
    elif len(set(saida)) != len(saida):
        print('Not invertible.')
    else:
        print('Invertible.')

numero = int(input())

while numero!=0:
    invertivel(numero)

    numero = int(input())
