x = list(map(str, input().split()))

while x != ['*']:
    b = True
    first = x[0][0].lower()
    for i in x:
        if i[0].lower() != first:
            b = False
            break

    if b:
        print('Y')
    else:
        print('N')

    x = list(map(str, input().split()))
