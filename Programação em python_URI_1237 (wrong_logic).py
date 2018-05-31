while True:
    try:
        string_1 = input()
        string_2 = input()
        if len(string_1) > len(string_2):
            a = string_2
            string_2 = string_1
            string_1 = a

        i = 0
        maximum = 0
        max_until_now = 0
        first_time = True
        while i != len(string_1):
            print(string_1[i])
            if string_1[i] in string_2 and first_time:
                max_until_now = 1
                index = string_2.index(string_1[i])
                first_time = False
            elif string_1[i] in string_2 and not first_time:
                if index + 1 == string_2.index(string_1[i]):
                    max_until_now += 1
                    index = string_1.index(string_1[i]) #vai achar o primeiro 'a' que aparecer, por exemplo
            else:
                if max_until_now > maximum:
                    maximum = max_until_now
                    max_until_now = 0
                    first_time = True
            i += 1

        if max_until_now > maximum:
            maximum = max_until_now

        print(maximum)

    except EOFError:
        break
