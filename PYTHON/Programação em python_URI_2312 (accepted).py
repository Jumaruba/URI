quantidade = int(input())
completo = []
medalhas = []
auxiliar = []
contador = 0
for i in range(0, quantidade):
    x = input()
    completo.append(x)
    x = x.split()
    jogos = [int(x[1]), int(x[2]), int(x[3])]
    if jogos in medalhas:
        contador+=1
    medalhas.append(jogos)


for j in range(0, len(medalhas)-contador):
    maior = max(medalhas)
    frequencia = medalhas.count(maior)
    if frequencia == 1:
        index = medalhas.index(maior)
        medalhas[index] = [-1]
        print(completo[index])
    elif frequencia > 1:
        for k in range(frequencia):
            index = medalhas.index(maior)
            auxiliar.append(completo[index])
            medalhas[index] = [-1]
        auxiliar.sort()
        for m in range(len(auxiliar)):
            print(auxiliar[m])
        auxiliar = []
