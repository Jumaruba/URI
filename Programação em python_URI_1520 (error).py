while True:
    try:
        quantidade = int(input())
        lista = []
        for j in range(quantidade):
            x, y = map(int, input().split())
            for i in range(x, y + 1):
                lista.append(i)
        lista.sort()
        quero = int(input())
        contador = 0
        if quero in lista:
            for index, numero in enumerate(lista):
                if numero == quero and contador == 0:
                    inicio = index
                    contador = 1
                    fim = inicio
                elif numero == quero and contador == 1:
                    fim = index
            print('%i found from %i to %i' % (quero, inicio, fim))
        else:
            print('%i not found' % quero)
    except:
        break

