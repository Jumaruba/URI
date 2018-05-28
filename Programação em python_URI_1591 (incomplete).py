testes = int(input())


def contando(palavra_inicio, palavra_quero):
    quantidade = 0
    for h in range(len(palavra_inicio) - len(palavra_quero) + 1):
        presenca = True
        for f in range(len(palavra_quero)):
            if palavra_quero[f] != palavra_inicio[f]:
                presenca = False
        if presenca == True:
            quantidade += 1
    return quantidade


def procura(palavra, matriz, colunas):
    quantidade = 0
    if len(palavra) == 1:
        for l in range(len(matriz)):
            if palavra in matriz[l]:
                quantidade += contando(matriz[l], palavra)

    else:
        for l in range(len(matriz)):
            if palavra in matriz[l]:
                quantidade += contando(matriz[l], palavra)
        for coluna in range(colunas):
            adicionar = ''
            for x in range(len(matriz)):
                adicionar += matriz[x][coluna]
            if palavra in adicionar:
                quantidade += contando(adicionar, palavra)

    return quantidade


for j in range(testes):
    linhas, colunas = map(int, input().split())

    matriz = [input() for k in range(linhas)]

    numero = int(input())
    for z in range(numero):
        n = procura(input(), matriz, colunas)
        print(n)
