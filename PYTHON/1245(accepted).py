while True:
    try:
        testes = int(input())
        dict = {}
        for i in range(testes):
            tamanho, pe = map(str, input().split())
            if tamanho in dict:
                dict[tamanho].append(pe)
            else:
                dict[tamanho] = []
                dict[tamanho].append(pe)
        total = 0
        for j in dict:
            e = dict[j].count('E')
            d = dict[j].count('D')
            total += min(d, e)

        print(total)

    except EOFError:
        break
