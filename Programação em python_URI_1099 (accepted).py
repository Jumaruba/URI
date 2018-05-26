n = int(input())
vetor = []
soma =0

for i in range (0,n):
    x,y = map(eval,input().split())
    if x<y:
        for j in range(x+1,y,1):
            if j%2==1:
                soma+=j
    elif y<x:
        for j in range(y + 1, x, 1):
            if j % 2 == 1:
                soma += j
    vetor.append(soma)
    soma = 0

for k in range(0,n):
    print(vetor[k])


