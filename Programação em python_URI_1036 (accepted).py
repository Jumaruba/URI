import math
A, B, C= input().slip()
A = float(A)
B = float(B)
C = float(C)

if A!=0:
    delta= (B*B)-(4*A*C)
    if delta>=0:
        R1 = (-B+math.sqrt(delta))/2*A
        R2 = (-B-math.sqrt(delta))/2*A
        print("R1 = %.5f" %R1)
        print("R2 = %.5f" %R2)
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")

