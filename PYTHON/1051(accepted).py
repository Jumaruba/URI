x = float(input())

if 0<=x<=2000:
    print("Isento")
elif 2000<x<=3000:
    taxa= (x-2000)*0.08
    print("R$ %.2f" %taxa)
elif 3000<x<=4500:
    taxa= (x-3000)*0.18+(1000*0.08)
    print("R$ %.2f" % taxa)
elif 4500<x:
    taxa= (x-4500)*0.28+1500*0.18+1000*0.08
    print("R$ %.2f" % taxa)

