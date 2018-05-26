x = int(input())
resposta = []

for  i in range (0,x):
    a,b,c = map(eval, input().split())
    ponderada = (a*2+b*3+c*5)/10
    ponderada = '%.1f' %ponderada
    resposta.append(ponderada)

resposta.append(0)

for j in range(0,x):
    print(resposta[j])
