a = str(input())
b = str(input())
c = str(input())

if a == "vertebrado":
    if b == "ave":
        if c== "carnivoro":
            print("aguia")
        elif c== "onivoro":
            print("pomba")
    elif b == "mamifero":
        if c== "herbivoro":
            print("vaca")
        elif c== "onivoro":
            print("homem")
elif a == "invertebrado":
    if b == "inseto":
        if c == "hematofago":
            print("pulga")
        elif c == "herbivoro":
            print("lagarta")
    if b == "anelideo":
        if c == "hematofago":
            print("sanguessuga")
        elif c == "onivoro":
            print("minhoca")
