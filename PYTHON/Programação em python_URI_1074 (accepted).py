n = int(input())
vpar = []
vsignal = []

for i in range (0,n):
    x = int(input())
    if x!=0:
        if x%2==0:
            vpar.append('EVEN')
        else:
            vpar.append('ODD')
        if x>0:
            vsignal.append('POSITIVE')
        else:
            vsignal.append('NEGATIVE')
    elif x==0:
        vpar.append('NULL')
        vsignal.append(0)

for i in range(0,n):
    if vsignal[i]!=0:
        print('%s %s' %(vpar[i], vsignal[i]))
    else:
        print('%s' %vpar[i])



