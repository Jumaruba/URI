import math
x, y, z= map(int, input().split())

maior2 = (x + y + math.fabs(x - y))/2
if maior2 == x:
    maior1 = y
else:
    maior1 = x

maior3 = (maior2 + z + math.fabs(maior2 - z))/2
if maior3 == maior2:
    maior2= z

k=maior2
maior2 = (maior1 + maior2 + math.fabs(maior1-maior2 ))/2
if maior2==maior1:
    maior1=k

print(int(maior1))
print(int(maior2))
print(int(maior3))
print()
print(x)
print(y)
print(z)
