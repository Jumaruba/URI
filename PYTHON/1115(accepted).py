x = 1
y = 1
vetor = []
k=0

while x!=0 and y!=0:
    x,y = map(eval, input().split())
    if x>0 and y>0:
        vetor.append('primeiro')
    elif x<0 and y>0:
        vetor.append('segundo')
    elif x<0 and y<0:
        vetor.append('terceiro')
    elif x>0 and y<0:
        vetor.append('quarto')
    elif x==0 or y==0:
        vetor.append('')
    k+=1

for i in range(0,k-1):
    print(vetor[i])