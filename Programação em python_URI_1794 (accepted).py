def an():
    if x <= r <= y:
        return True
    return False


r = int(input())
x, y = map(int, input().split())
b = an()
x, y = map(int, input().split())
if b:
    b = an()
if b:
    print('possivel')
else:
    print('impossivel')
