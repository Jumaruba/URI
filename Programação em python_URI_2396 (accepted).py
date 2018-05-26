quantidade, voltas = map(int,input().split())
matriz = []
resultado = []
for i in range(0, quantidade):
    tempo = list(map(int, input().split()))
    matriz.append(tempo)
for k in range(0, quantidade):
    resultado.append(sum(matriz[k]))
for j in range(0, 3):
    print(resultado.index(min(resultado))+1)
    resultado[resultado.index(min(resultado))] = max(resultado)+1
