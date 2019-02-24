def posicao(pos):
    if pos == 0:
        print('A')
    elif pos == 1:
        print('B')
    else:
        print('C')


while True:
    try:
        lista = list(map(int, input().split()))

        if lista[0] == lista[1] == lista[2]:
            print('*')
        else:
            termos_1 = lista.count(1)
            if termos_1 == 1:
                pos = lista.index(1)
                posicao(pos)
            else:
                pos = lista.index(0)
                posicao(pos)
    except EOFError:
        break
