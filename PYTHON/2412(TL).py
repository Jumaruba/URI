def distancia(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def possivel(q, lista_a, linhas_a):
    recebe_1 = []
    recebe_0 = False
    for n in range(linhas_a):
        caminho = distancia(lista_a[q], lista_a[n])
        if caminho <= tamanho and caminho != 0:
            recebe_0 = True
            recebe_1.append(n)
    return recebe_0, recebe_1


def const_dicionario(linhas):
    dicionario = {}
    for m in range(linhas):
        dicionario[m] = []
    return dicionario


def profundidade(n, marcado):  # visitar no n
    marcado.append(n)
    for p in dicionario[n]:
        if p not in marcado:
            profundidade(p, marcado)
    return marcado


def const_parametro(linhas):
    parametro = []
    for b in range(linhas):
        parametro.append(b)
    return parametro


lista = []
linhas, tamanho = map(int, input().split())
consegue = True
dicionario = const_dicionario(linhas)

for i in range(linhas):  # criando lista com os pontos
    ponto = list(map(int, input().split()))
    lista.append(ponto)

for j in range(linhas):
    consegue, numero = possivel(j, lista, linhas)
    dicionario[j]+=numero
    if not consegue:
        break

quero = []
quero = profundidade(0, quero)
quero.sort()
parametro = const_parametro(linhas)


if not consegue or quero != parametro:
    print('N')
else:
    print('S')