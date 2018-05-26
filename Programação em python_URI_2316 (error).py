postos, carros, leituras = map(int, input().split())
posicao = []
empate = []
auxiliar = []
resposta = []
for j in range(carros):
    posicao.append(0)
    empate.append(0)
    auxiliar.append(leituras+1)
for i in range(leituras):
    lugar, y = map(int, input().split())
    index = lugar - 1
    if (posicao[index] + 1) in posicao:  # em caso de empate
        vezes = posicao.count(posicao[index])
        empate[index] = vezes
    else:
        empate[index] = 0
    if (posicao[index] + 1) % postos == y % postos:
        posicao[index] += 1
for k in range(len(set(posicao))):
    maior = posicao.index(max(posicao))
    vezes = posicao.count(max(posicao))
    if vezes > 1:
        for k in range(vezes):
            posicao[maior] = -1
            auxiliar[maior] = empate[maior]
            maior = posicao.index(max(posicao))
        for m in range(vezes):
            resposta.append(auxiliar.index(min(auxiliar))+1)
            auxiliar[auxiliar.index(min(auxiliar))] = 300
    else:
        resposta.append(maior + 1)
        posicao[maior] = -1

for u in range(len(resposta)-1):
    print(resposta[u], end=' ')
print(resposta[len(resposta)-1])
# preciso identificar quem fez a posicao primeiro

'''4 9 113
1 2
1 4
5 3
7 3
8 3
9 3
8 2
5 4
7 1
8 3
1 4
6 1
3 1
8 2
6 4
6 4
8 2
8 3
6 2
6 1
6 1
8 2
9 2
9 1
8 1
1 3
6 2
4 2
6 3
9 1
9 1
4 4
1 4
2 1
9 1
6 3
6 4
8 4
8 2
9 3
9 3
9 1
1 3
1 2
9 1
9 2
5 1
5 4
5 3
4 4
5 1
4 1
5 4
5 4
5 3
1 1
4 1
4 4
1 4
5 3
5 2
5 4
5 4
4 3
4 2
4 2
1 4
4 4
4 4
5 3
5 2
5 4
4 1
1 3
4 1
4 2
4 3
1 3
1 3
1 3
1 4
1 2
1 4
1 2
1 1
1 3
1 1
1 2
1 2
1 4
1 4
1 3
1 3
1 3
1 4
1 2
1 4
1 2
1 1
1 4
1 1
1 4
1 4
1 1
1 4
1 3
1 2
1 4
1 2
1 3
1 2
1 3
1 4

1 6 5 4 8 9 7 3 2'''

# nesse caso o 6 fez assumiu a posicao 4 primeiro
