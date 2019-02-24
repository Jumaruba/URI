j, r = map(int, input().split())
jogadores = [0 for k in range(j)]
lista = list(map(int, input().split()))
contador = 0
for i in lista:
    jogadores[contador]+=i
    contador+=1
    if contador%j==0:
        contador = 0
print(jogadores.index(max(jogadores))+1)