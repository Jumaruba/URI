while True:
    try:
        quantidade = int(input())
        x = sorted([input() for i in range(quantidade)])
        for j in x:
            print(j)
    except:
        break
