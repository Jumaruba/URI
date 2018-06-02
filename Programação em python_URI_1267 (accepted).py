colunas, linhas = map(int, input().split())

while linhas != 0 and colunas != 0:
    comp = [x for x in range(colunas)]
    x = 0
    for i in range(linhas):
        linha = list(map(int, input().split()))
        comp = [x for x in comp if linha[x] == 1]
        x = 0

    if comp:
        print('yes')
    else:
        print('no')
    colunas, linhas = map(int, input().split())
