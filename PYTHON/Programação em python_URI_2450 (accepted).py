linhas, colunas = map(int, input().split())
contador = -1
contador_anterior = -1
resposta = True


def lista_zero(colunas):
    lista = []
    for i in range(colunas):
        lista.append(0)
    return lista


parametro = lista_zero(colunas)
caso_zero = False
for i in range(linhas):
    x = list(map(int, input().split()))
    if x != parametro and caso_zero == False:
        numero = 0
        while numero == 0 and resposta:
            contador += 1
            numero = x[contador]
        if contador <= contador_anterior:
            resposta = False
        contador_anterior = contador
        contador = 0
    else:
        caso_zero = True
        if x != parametro:
            resposta = False

if resposta:
    print('S')
else:
    print('N')
