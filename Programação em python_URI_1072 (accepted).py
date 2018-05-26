n = int(input())
in1=0
out=0

for i in range (0,n):
    x = int(input())
    if 10<=x<=20:
        in1+=1
    else:
        out+=1

print("%i in" %in1)
print("%i out" %out)
