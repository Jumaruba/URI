def sum_coluna(linhas, matriz, c):
    soma = 0
    for li in range(linhas):
        soma += matriz[li][c]
    return soma


linhas, colunas = map(int, input().split())

matriz = [list(map(int, input().split())) for i in range(linhas)]

sum_now = 0
max_sum = 0

for l in range(linhas):
    sum_now = sum(matriz[l])
    if sum_now > max_sum:
        max_sum = sum_now

for c in range(colunas):
    sum_now = sum_coluna(linhas, matriz, c)
    if sum_now > max_sum:
        max_sum = sum_now

print(max_sum)