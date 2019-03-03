casas, entregas = map(int, input().split())
dicionario = {}
enderecos = list(map(int, input().split()))
caminho = list(map(int, input().split()))

for i in range(casas):
    dicionario[enderecos[i]] = i

inicio = enderecos[0]
dist = 0
for n in caminho:
    dist += abs(dicionario[inicio] - dicionario[n])
    inicio = n

print(dist)
