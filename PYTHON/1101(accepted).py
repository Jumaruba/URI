fim, inicio = map(int, input().split())
while fim > 0 and inicio > 0:
    if fim < inicio:
        b = fim
        fim = inicio
        inicio = b
    soma = 0
    for i in range(inicio, fim + 1):
        print(i, end=' ')
        soma += i
    print('Sum=%i' % soma)
    fim, inicio = map(int, input().split())
