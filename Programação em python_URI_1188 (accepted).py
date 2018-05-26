def matriz():
    vetor = []
    for i in range(0, 12):
        vetor.append([])
        for j in range(0, 12):
            vetor[i].append(float(input()))
    return vetor


def soma_esquerda(vetor):
    soma = 0
    for i in range(11, 6, -1):
        for j in range(-i, -6, +1):
            soma += vetor[i][j]
    return soma


def soma_direita(vetor):
    soma = 0
    for i in range(11, 6, -1):
        for j in range(6, i):
            soma += vetor[i][j]
    return soma

letra = str(input())
vetor = matriz()
soma = soma_esquerda(vetor)
soma += soma_direita(vetor)

if letra == 'S':
    print('%.1f' % soma)
else:
    print('%.1f' % (soma / 30))
