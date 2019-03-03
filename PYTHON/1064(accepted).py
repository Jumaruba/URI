vetor =[]
k=0
soma=0
for i in range (0,6):
    x= float(input())
    if x>0:
        vetor.append(x)

k=len(vetor)
print("%i valores positivos" %k)

for j in range (0,k):
    soma+=vetor[j]

media=soma/k
print('%.1f' %media)
