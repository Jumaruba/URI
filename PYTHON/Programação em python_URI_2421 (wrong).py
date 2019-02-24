def tentativa():
    if c_f1 <= com_f and c_f2 <= com_f and h_f1 + h_f2 <= h_f:  # normal
        return True
    elif h_f1 <= com_f and c_f2 <= com_f and c_f1 + h_f2 <= h_f:  # girando a primeira foto
        return True
    elif c_f1 <= com_f and h_f2 <= com_f and h_f1 + c_f2 <= h_f:  # girando a segunda foto
        return True
    elif c_f1 + c_f2 <= h_f and h_f1 <= com_f and h_f2 <= com_f:  # girando as duas fotos
        return True
    return False


h_f, com_f = map(int, input().split())
h_f1, c_f1 = map(int, input().split())
h_f2, c_f2 = map(int, input().split())

bol = tentativa()
k = h_f
h_f = com_f
com_f = k

bol = tentativa()

if bol:
    print('S')
else:
    print('N')
