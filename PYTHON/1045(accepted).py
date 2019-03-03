x,y,z = map(float, input().split())

for i in [x,y,z]:
    for j in [x,y,z]:
        for k in [x,y,z]:
            if i>j>k:
                a=i
                b=j
                c=k


print (a, b, c)