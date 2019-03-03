total, rodadas = map(eval, input().split())
d = total
e = total
f = total
for i in range (0, rodadas):
    operacao = list(map(str, input().split()))
    if operacao[0]=='C':
        operacao[2] = int(operacao[2])
        if operacao[1] == 'D':
            d -= operacao[2]
        elif operacao[1] == 'E':
            e -= operacao[2]
        elif operacao[1] == 'F':
            f -= operacao[2]
    elif operacao[0]=='V':
        operacao[2]=int(operacao[2])
        if operacao[1]=='D':
            d +=operacao[2]
        elif operacao[1]=='E':
            e+=operacao[2]
        elif operacao[1]=='F':
            f+=operacao[2]
    elif operacao[0]=='A':
        operacao[3]= int(operacao[3])
        if operacao[2] == 'D':
            d -= operacao[3]
        elif operacao[2] == 'E':
            e -= operacao[3]
        elif operacao[2] == 'F':
            f -= operacao[3]
        if operacao[1]=='D':
            d +=operacao[3]
        elif operacao[1]=='E':
            e+=operacao[3]
        elif operacao[1]=='F':
            f+=operacao[3]
    operacao=[]
print(d,e,f)


