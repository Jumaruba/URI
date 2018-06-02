n = int(input())

while n != 0:
    x = list(map(int, input().split()))
    x[x.index(max(x))] = -1
    print(x.index(max(x))+1)

    n = int(input())
