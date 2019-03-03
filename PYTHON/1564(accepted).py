while True:
    try:
        x = int(input())
        if x == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
    except EOFError:
        break