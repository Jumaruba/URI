testes = int(input())
times = []
pontos = []
vitorias = []
gols = []

for i in range(0, testes):
    quant_times, quant_jogos = map(int, input().split())
    for i in range(0, quant_times):
        x = str(input())
        times.append(x)

    for j in range(0, quant_jogos):
        gols_1, time_1, gols_2, time_2 = map(str, input().split())
        gols_1 = int(gols_1)
        gols_2 = int(gols_2)

        index_1 = times.index(time_1)
        index_2 = times.index(time_2)

        gols.insert(index_1, gols[index_1]+gols_1)
        gols.insert(index_2, gols[index_2]+gols_2)

        if gols_1 > gols_2:
            vitorias.insert(index_1, vitorias[index_1] + 1)
            pontos.insert(index_1, pontos[index_1] + 3)
        elif gols_2 > gols_1:
            vitorias.insert(index_2, vitorias[index_2] + 1)
            pontos.insert(index_2, pontos[index_2] + 3)
        else:
            pontos.insert(index_2, pontos[index_2] + 1)
            pontos.insert(index_1, pontos[index_1] + 1)
    primeiro_lugar = max(pontos)
    if vitorias.count(primeiro_lugar)>1:
        for k in range (0,vitorias.count(primeiro_lugar)):
            x = pontos.index(primeiro_lugar)

