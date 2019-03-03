import math
a, b ,c= map(eval, input().split())

maior1 = ( a + b + math.fabs(a - b))/2
maior2 = (maior1 + c + math.fabs(maior1 - c))/2

print("%i eh o maior" %maior2)