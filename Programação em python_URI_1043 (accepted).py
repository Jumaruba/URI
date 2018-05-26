a, b,c =map(float, input().split())

if a+b>c and c+b>a and a+c>b:
    p=a+b+c
    print("Perimetro = %.1f" %p)
else:
    h=(a+b)*c/2
    print("Area = %.1f" %h)