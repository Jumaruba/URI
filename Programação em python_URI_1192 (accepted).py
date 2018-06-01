for i in range(int(input())):
    x = str(input())
    l = x[1].upper()
    if x[0] == x[2]:
        print(int(x[0]) * int(x[2]))
    elif x[1] == l:
        print(int(x[2]) - int(x[0]))
    else:
        print(int(x[0]) + int(x[2]))
