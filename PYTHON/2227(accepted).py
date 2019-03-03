airports, linhas = map(int, input().split())
count = 1

while airports != 0 and linhas != 0:
    matriz = [0 for i in range(airports)]

    for j in range(linhas):
        aer_1, aer_2 = map(int, input().split())
        matriz[aer_1 - 1] += 1
        matriz[aer_2 - 1] += 1

    maior = max(matriz)
    times = matriz.count(maior)
    print('Teste {}'.format(count))

    for m in range(times):
        index = matriz.index(maior)
        print(index + 1, end=' ')
        matriz[index] = -1

    count += 1
    airports, linhas = map(int, input().split())
    print('')
    print('')
