x = int(input())
for i in range(x):
    x, y = map(int, input().split())
    if x != 0 or y != 0:
        print(26 ** x * 10 ** y)
    else:
        print(0)
