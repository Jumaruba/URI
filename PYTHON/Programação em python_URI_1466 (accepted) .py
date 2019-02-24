def busca(vertice, numero):
    if numero > vertice:  # numero fica à direita
        if dicionario[vertice][1] == '':
            dicionario[vertice][1] = numero
            dicionario[numero] = ['', '']
        else:
            busca(dicionario[vertice][1], numero)  # se ja estiver preenchido, aplicamos na sub-arvore
    if numero < vertice:  # fica à esquerda
        if dicionario[vertice][0] == '':
            dicionario[vertice][0] = numero
            dicionario[numero] = ['', '']
        else:
            busca(dicionario[vertice][0], numero)
    return dicionario


def largura(prof, numero):
    prof += 1
    for x in dicionario[numero]:
        if len(vetor) < prof:
            vetor.append([])
            if x != '':
                vetor[prof - 1].append(x)
                largura(prof, x)
        else:
            if x != '':
                vetor[prof - 1].append(x)
                largura(prof, x)
    return vetor


cases = int(input())
for n in range(cases):
    qualquer = int(input())
    lista = list(map(int, input().split()))

    vetor = [[lista[0]]]
    dicionario = {lista[0]: ['', '']}

    for i in range(1, qualquer):
        dicionario = busca(lista[0], lista[i])

    vetor = largura(1, lista[0])

    vetor.remove([])
    print('Case %i:' % (n + 1))
    for j in range(len(vetor) - 1):
        for k in range(len(vetor[j])):
            print(vetor[j][k], end=' ')
    for m in range(len(vetor[-1]) - 1):
        print(vetor[-1][m], end=' ')
    print(vetor[-1][-1])
    print('')
