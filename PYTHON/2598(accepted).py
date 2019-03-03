import math

x = int(input())

for i in range(x):
    j, w = map(int, input().split())
    print(math.ceil(j/w))