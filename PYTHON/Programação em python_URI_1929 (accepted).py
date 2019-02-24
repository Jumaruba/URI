x1, x2, x3, x4 = map(int, input().split())
a = False


def triangulo(a, b, c):
    if a < b + c and c < a + b and b < c + a:
        return True


a = triangulo(x1, x2, x3)
b = triangulo(x1, x2, x4)
d = triangulo(x2, x3, x4)
e = triangulo(x1, x4, x3)
if a == True or b==True or d==True or e==True:
    print('S')
else:
    print('N')
