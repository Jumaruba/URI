cases = int(input())

for i in range(cases):
    game1 = input()
    time1 = int(game1[0])
    time2 = int(game1[4])
    game2 = input()
    time2_ = int(game2[0])
    time1_ = int(game2[4])
    if time1_+time1 > time2_+time2:
        print('Time 1')
    elif time2+time2_ > time1_+time1:
        print('Time 2')
    else:
        if time2>time1_:
            print('Time 2')
        elif time1_>time2:
            print('Time 1')
        else:
            print('Penaltis')