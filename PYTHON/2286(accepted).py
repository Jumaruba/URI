vetor=[]
vetor2=[]
soma=0
n=1
while n!=0:
    x = int(input())
    if x != 0:
        par = str(input())
        impar = str(input())
        vetor2.append(x)
        for i in range (0, x):
            par1, impar1 = map(int, input().split())
            total=par1+impar1
            if total%2==0:
                vetor.append(par)
            else:
                vetor.append(impar)
    elif x==0:
        n=0
k=0
for j in range (0,len(vetor2)):
    print('Teste %i' % (j + 1))
    for w in range (k, vetor2[j]+k):
        print(vetor[k])
        k+=1
    print('')





