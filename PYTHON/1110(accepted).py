def carta_sobrante(x):
    vetor = []
    descartadas = []
    for i in range(1, x + 1):
        vetor.append(i)
    for j in range(1, x):
        descartada = vetor.pop(0)
        descartadas.append(descartada)
        final = vetor.pop(0)
        vetor.append(final)
    return vetor[0], descartadas



x = int(input())

while x != 0:
    sobrou, descartadas = carta_sobrante(x)
    print('Discarded cards:', str(descartadas)[1:len(str(descartadas))-1])
    print('Remaining card:', sobrou)
    x = int(input())