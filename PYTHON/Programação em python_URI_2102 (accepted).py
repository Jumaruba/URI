def const_dicionario(linhas):
    dicionario = {}
    for i in range(linhas):
        x = list(map(int,input().split()))
        if '%i %i' %(x[1], x[2]) not in dicionario:
            dicionario['%i %i' %(x[1], x[2])] = 0
        dicionario['%i %i' %(x[1], x[2])] += x[3]

    return dicionario

def main():
    lista = []
    numero, linhas = map(int, input().split())
    dicionario = const_dicionario(linhas)

    for j in dicionario:
        lista.append([j, dicionario[j]])
    lista.sort()
    for k in range(len(lista)):
        print(lista[k][0], lista[k][1])


quantidade = int(input())
lista = []

for i in range(quantidade-1):
    main()
    print('')

main()
