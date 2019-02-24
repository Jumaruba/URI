x = int(input())
l = list(map(int, input().split()))

try:
    for i in range(1,x+1):
        l.remove(i)
except:
    print(i)
