def dicionario_inicio(quantidade):
    for i in range(1,quantidade+1):
        dicionario[i] = []
    return dicionario

def dicionario_fim(linhas):
    for i in range(linhas):
        x, y = map(int,input().split())
        dicionario[x] += [y]
        dicionario[y] +=[x]
    return dicionario

def profundidade(n,marcado):
    marcado.append(n)
    for i in dicionario[n]:
        if i not in marcado:
            profundidade(i,marcado)
    return marcado

quantidade, linhas = map(int,input().split())
dicionario = {}
while True:
    try:
        dicionario = dicionario_inicio(quantidade)
        dicionario = dicionario_fim(linhas)
        numero = int(input())
        marcado = []
        marcado = profundidade(numero,marcado)
        print(len(marcado))
        quantidade, linhas = map(int,input().split())
        dicionario = {}

    except:
        break
