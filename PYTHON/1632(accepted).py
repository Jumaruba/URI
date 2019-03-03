tests = int(input())
special_letters = ['a', 'e', 'i', 'o', 's']
for i in range(tests):
    sum_letters = 0
    word = input()
    for j in special_letters:
        number = word.count(j.upper())
        number += word.count(j.lower())
        sum_letters += number
    possible = (2 ** (len(word) - sum_letters)) * (3 ** sum_letters)

    print(possible)
