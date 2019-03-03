x, y=map(int,input().split())

if x>y:
    tempo= 24-x+y
    print("O JOGO DUROU %i HORA(S)" %tempo)
if x<y:
    tempo= y-x
    print("O JOGO DUROU %i HORA(S)" %tempo)
if x==y:
    print("O JOGO DUROU 24 HORA(S)")