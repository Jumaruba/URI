cases = int(input())

for i in range(cases):
    x = input().split()
    if x[0] == 'Thor' and x[1] != 0:
        print('Y')
    else:
        print('N')
