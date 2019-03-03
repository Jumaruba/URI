bancos, linhas = map(int, input().split())
lista = []
for i in range(bancos):
    lista.append([str(i+1)])

for j in range(linhas):
    modo, empresa1, empresa2 = input().split()
    if modo == 'F':
        n1, n2 = -1, -1
        contador = 0
        while n1 == -1 or n2 == -1:
            if empresa1 in lista[contador]:
                n1 = contador
            elif empresa2 in lista[contador]:
                n2 = contador
            contador += 1
        lista[n1] += lista[n2]
        lista.remove(lista[n2])
    else:
        k = True
        contador = 0
        while k and contador < len(lista):
            if empresa1 in lista[contador]:
                if empresa2 in lista[contador]:
                    print('S')
                else:
                    print('N')
                k = False
            elif empresa2 in lista[contador]:
                if empresa1 in lista[contador]:
                    print('S')
                else:
                    print('N')
                    k = False
            contador += 1
