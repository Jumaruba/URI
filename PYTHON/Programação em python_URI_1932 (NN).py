quantidade, cota = map(int, input().split())

lista = list(map(int, input().split()))
min_ate_agora = max_ate_agora = lista[0]
lucro = 0
for i in range(1, quantidade):
    if (min_ate_agora > lista[i] and max_ate_agora - lista[i] >= cota) or lista[i] < min_ate_agora:
        if max_ate_agora - min_ate_agora - cota > 0:
            lucro += max_ate_agora - min_ate_agora - cota
        max_ate_agora = min_ate_agora = lista[i]
    if lista[i] > max_ate_agora:
        max_ate_agora = lista[i]

    if max_ate_agora - min_ate_agora - cota > 0:
        lucro += max_ate_agora - min_ate_agora - cota
print(lucro)
