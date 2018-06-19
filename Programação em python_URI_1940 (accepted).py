jogadores, rodadas = map(int, input().split())
lista = list(map(int, input().split()))
contador = 0
dicionario = [0 for k in range(jogadores)]
for i in range(len(lista)):
    if contador % jogadores == 0:
        contador = 0
    dicionario[contador] += lista[i]
    contador += 1

x = dicionario.count(max(dicionario))
if x > 1:
    for j in range(x - 1):
        dicionario[dicionario.index(max(dicionario))] = 0
    print(dicionario.index(max(dicionario))+1)
else:
    print(dicionario.index(max(dicionario))+1)
