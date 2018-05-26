x = int(input())

def quadrado_cubo(x):
    for i in range(1,x+1):
        print(i, end=' ')
        print(i**2, end=' ')
        print(i**3)

quadrado_cubo(x)