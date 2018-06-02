for i in range(int(input())):
    x1, x2 = map(str, input().split())
    lx1 = len(x1)
    lx2 = len(x2)
    if lx1 >= lx2:
        n_letter = ''.join([x1[j] for j in range(-lx2, 0)])
        if n_letter == x2:
            print('encaixa')
        else:
            print('nao encaixa')
    else:
        print('nao encaixa')
