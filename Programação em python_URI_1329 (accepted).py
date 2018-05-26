partidas = int(input())

while partidas!=0:
    jogadas = list(map(int,input().split()))
    joao = 0
    maria = 0
    for i in range(0,len(jogadas)):
        if jogadas[i]==0:
            maria+=1
        elif jogadas[i]==1:
            joao+=1

    print('Mary won %i times and John won %i times' %(maria,joao))
    partidas = int(input())