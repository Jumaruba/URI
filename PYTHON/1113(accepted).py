k=0
vetor = []
y = 1
x = 0
while x!=y:
    x,y=map(eval,input().split())
    if x>y:
        vetor.append('Decrescente')
    elif x<y:
        vetor.append('Crescente')
    if x!=y:
        k+=1


for i in range (0,k):
    print(vetor[i])