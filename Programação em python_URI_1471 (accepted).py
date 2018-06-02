while True:
    try:
        inicial, final = map(int, input().split())
        lista = list(map(int, input().split()))
        if inicial != final:
            lista_final = [j for j in range(1, inicial + 1) if j not in lista]
            for i in range(len(lista_final)):
                print(lista_final[i], end=' ')
            print('')
        else:
            print('*')
    except EOFError:
        break
