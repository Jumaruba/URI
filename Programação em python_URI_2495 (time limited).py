def lista(x):
    lista = []
    for i in range(1, x + 1):
        lista.append(i)
    return lista


while True:
    try:
        x = int(input())
        listas = lista(x)
        while len(listas) != 1:
            termos = map(int, input().split())
            for j in termos:
                listas.remove(j)
        print(listas[0])
    except EOFError:
        break
