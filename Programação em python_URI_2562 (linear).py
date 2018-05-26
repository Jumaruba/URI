L = []

quantidade, linhas = map(int, input().split())

while True:
    try:
        x1, x2 = map(int, input().split())
        L.append([x1, x2])
        for i in range(linhas - 1):
            l2 = []
            l1 = []
            x1, x2 = map(int, input().split())
            for l in L:
                if x1 in l:
                    l1 = l
                if x2 in l:
                    l2 = l
                if l1 != []:
                    if l2 != []:
                        if l1 != l2:
                            l1 += l2
                    else:
                        l1.append(x2)

                else:
                    if l2 != []:
                        l2.append(x1)
                    else:
                        L.append([x1, x2])

        numero = int(input())
        contador = 0
        for i in L:
            if numero in i:
                print(len(i))
                contador = 1
                break
        if contador == 0:
            print(1)
        quantidade, linhas = map(int, input().split())
        L = []

    except:
        break
