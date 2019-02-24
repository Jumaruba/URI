dia_inicio, dinheiro_inicio, var, futuro = map(int, input().split())

if dia_inicio % 2 == 1:
    if futuro % 2 == 0:
        print(dinheiro_inicio)
    else:
        print(dinheiro_inicio + var)
else:
    if futuro % 2 == 1:
        print(dinheiro_inicio - var)
    else:
        print(dinheiro_inicio)
