a,b = input().split()
a = int(a)
b = int(b)

if a==1:
    total=b*4
elif a==2:
    total = b *4.5
elif a==3:
    total = b *5
elif a==4:
    total = b *2
elif a==5:
    total = b *1.5

print("Total: R$ %.2", %total)
