for i in range(int(input())):
    x = input()
    if len(x) == 5:
        print(3)
    elif (x[0] == 'o' and x[2] == 'e') or (x[0] == 'o' and x[1] == 'n') or (x[1] == 'n' and x[2] == 'e'):
        print(1)
    else:
        print(2)
