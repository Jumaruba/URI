x, y = map(int, input().split())


def num_linhas(x, y):
    if y % x == 0:
        return y // x
    else:
        return y // x + 1

num = num_linhas(x,y)

for i in range(0,num):
    primeiro = (i*x)+1
    for j in range(0,x-1):
        if primeiro+j>y:
            break
        else:
            print(primeiro+j, end=' ')
    print(primeiro+x-1)



