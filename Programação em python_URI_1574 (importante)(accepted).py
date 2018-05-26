casos = int(input())
fim = []

for i in range(0, casos):
    x = int(input())
    posicao = 0
    lista = []
    for j in range(0, x):
        comando = str(input())
        if comando == 'LEFT':
            lista.append(-1)
        elif comando == 'RIGHT':
            lista.append(1)
        else:
            if len(comando) == 10:
                comando = (int(comando[8]) * 10) + (int(comando[9]) - 1)
            else:
                comando = int(comando[8]) - 1
            lista.append(lista[comando])

    print(sum(lista))

#ERRO ANTERIOR: NAO ESTAVA CONSIDERANDO OS CASOS DO SAME AS X ONDE O X PODIA SER MAIOR QUE 10
