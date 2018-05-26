while True:
    try:
        modelos, prejudicados = map(int, input().split())
        x = list(map(int, input().split()))
        soma = 0
        for i in range(0, prejudicados):
            valor = max(x)
            soma += valor
            pos = x.index(valor)
            x[pos] = -1

        print(soma)
    except EOFError:
        break
