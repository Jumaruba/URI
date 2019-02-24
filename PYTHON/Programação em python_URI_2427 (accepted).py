def quantidade(barra, soma):
    barra = barra // 2
    if barra < 2:
        return soma
    else:
        soma *= 4
        return quantidade(barra, soma)


lado = int(input())

print(quantidade(lado, 4))
