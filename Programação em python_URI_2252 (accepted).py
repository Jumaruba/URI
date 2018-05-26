def senha():
    global z, x
    oleo = list(map(float, input().split()))
    senha_final = []
    print('Caso %i:' % z, end=' ')
    for i in range(0, x):
        k = max(oleo)
        pos = oleo.index(k)
        oleo[pos] = -1
        senha_final.append(pos)

    for j in range(0, x - 1):
        print(senha_final[j], end='')
    print(senha_final[x - 1])


z = 1
x = int(input())
while True:
    try:
        senha()
        x = int(input())
        z += 1
    except EOFError:
        break