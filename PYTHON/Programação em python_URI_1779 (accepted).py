def sequenciais(notas, maior):
    contador = 1
    contador_max = 1
    for i in range(notas.index(maior) + 1, len(notas)):
        if notas[i] == maior:
            contador += 1
        elif notas[i] != maior:
            if contador > contador_max:
                contador_max = contador
            contador = 0
        if contador > contador_max:
            contador_max = contador

    return contador_max


testes = int(input())

for i in range(testes):
    quantidade = int(input())
    notas = list(map(int, input().split()))

    maior = max(notas)
    contador = sequenciais(notas, maior)
    print('Caso #%i: %i' % (i + 1, contador))
