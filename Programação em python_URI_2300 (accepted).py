def dic_inicio(vertices):
    dicionario = {}
    for j in range(1, vertices + 1):
        dicionario[j] = []
    return dicionario


def dic_const(linhas):
    dicionario = dic_inicio(vertices)
    for i in range(linhas):
        x, y = map(int, input().split())
        dicionario[x] += [y]
        dicionario[y] += [x]
    return dicionario


def profundidade(n):  # visitar no n
    marcado.append(n)
    for i in dicionario[n]:
        if i not in marcado:
            profundidade(i)
    return marcado


def esperado(vertices):
    lista_esperada = []
    for i in range(1, vertices + 1):
        lista_esperada.append(i)
    return lista_esperada


vertices, linhas = map(int, input().split())
marcado = []
contador = 1

while vertices != 0 and linhas != 0:

    dicionario = dic_const(linhas)
    lista = profundidade(1)
    lista = sorted(lista)
    lista_esperada = esperado(vertices)

    print('Teste %i' % contador)
    if lista_esperada == lista:
        print('normal')

    else:
        print('falha')
    vertices, linhas = map(int, input().split())
    contador += 1
    print('')
    marcado = []