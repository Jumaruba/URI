x1, x2 = map(int, input().split())

while x1 != 0 and x2 != 0:
    x1_v = list(map(str, input().split()))
    x2_v = list(map(str, input().split()))
    total = 0
    x = set(x1_v)
    y = set(x2_v)
    if len(x) > len(y):
        b = x
        x = y
        y = b
    for i in x:
        if i not in y:
            total += 1
    print(total)
    x1, x2 = map(int, input().split())
