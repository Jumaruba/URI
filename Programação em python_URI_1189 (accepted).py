def matriz():
    vetor = []
    for i in range(0, 12):
        vetor.append([])
        for j in range(0, 12):
            vetor[i].append(float(input()))
    return vetor


def soma_cima(vetor):
    soma = 0
    for i in range(1, 6):
        for j in range(0, i):
            soma += vetor[i][j]
    return soma


def soma_baixo(vetor):
    soma = 0
    for i in range(6, 11):
        for j in range(0, 11 - i):
            soma += vetor[i][j]
    return soma


letra = str(input())
vetor = matriz()
soma = soma_cima(vetor)
soma += soma_baixo(vetor)

if letra == 'S':
    print('%.1f' % soma)
else:
    print('%.1f' % (soma / 30))
