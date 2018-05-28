while True:
    try:
        sentence = input()
        new_sentence = ''
        contador = 0
        for i in sentence:
            if i != ' ' and contador % 2 == 0:
                new_sentence += i.upper()
                contador += 1
            elif i != ' ' and contador % 2 == 1:
                new_sentence += i.lower()
                contador += 1
            elif i == ' ':
                new_sentence += ' '


        print(new_sentence)

    except:
        break