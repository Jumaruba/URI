casas, entregas = map(int, input().split())

enderecos = list(map(int, input().split()))
caminho = list(map(int,input().split()))
index_anterior = 0
distancia = 0

for i in caminho:
    index_sucessor = enderecos.index(i)
    distancia += abs(index_sucessor-index_anterior)
    index_anterior = index_sucessor

print(distancia)