x = list(map(int,input().split()))
y = list(map(int,input().split()))

bo = True
for i in range(0,len(x)):
    if x[i]==y[i]:
        bo= False

if bo == False:
    print('N')
else:
    print('Y')