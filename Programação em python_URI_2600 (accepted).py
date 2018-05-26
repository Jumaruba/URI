testes = int(input())

for i in range(0, testes):
    k = True
    cima = int(input())
    x1,x2,x3,x4 = map(int,input().split())
    baixo = int(input())
    for j in [cima, baixo, x1, x2, x3, x4]:
        if j==7 or j==0:
            k = False
    if cima!=baixo!=x1!=x2!=x3!=x4 and k == True:
        if baixo + cima == 7:
            if x1 + x3 == 7 and x2 + x4 == 7:
                print('SIM')
            else:
                print('NAO')
        else:
            print('NAO')
    else:
        print('NAO')