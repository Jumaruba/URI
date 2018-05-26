x1,x2,x3,x4,x5 = map(int,input().split())

if x1>x2>x3>x4>x5:
    print('D')
elif x1<x2<x3<x4<x5:
    print('C')
else:
    print('N')