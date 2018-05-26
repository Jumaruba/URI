k = 0
vetor = []
x = 0
while x!=2002:
    x = int(input())
    if x!=2002:
        vetor.append('Senha Invalida')
    elif x==2002:
        vetor.append('Acesso Permitido')
    k+=1

for i in range (0,k):
    print(vetor[i])

