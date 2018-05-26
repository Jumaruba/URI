def lista(numeros):
    vetor = []
    for i in range(numeros):
        vetor.append(int(input()))
    vetor.sort()
    return vetor


numeros, testes = map(int, input().split())
contador = 1
while numeros != testes != 0:
    print('CASE# %i:' % contador)
    marmores = lista(numeros)
    for i in range(testes):
        teste = int(input())
        if teste in marmores:
            index = marmores.index(teste)
            print('%i found at %i' % (teste, index + 1))
        else:
            print('%i not found' % (teste))
    numeros, testes = map(int, input().split())
    contador+=1