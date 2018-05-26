x= int(input())
for i in range(0,x):
    Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, RX, RY = map(int,input().split())
    if Ax<=RX<=Bx and Ay<=RY<=Dy:
        print(1)
    else:
        print(0)