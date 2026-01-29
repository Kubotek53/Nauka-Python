imie = input("Wpisz swoje imię: ")
imie1 = imie
while imie != True:
    imie = bool(imie)
    if imie:
        print(f"Twoje imię to: {imie1}")
        exit()
    else:
        imie = input("Nie wpisałeś swojego imienia. Wpisz jeszcze raz: ")
        imie1 = imie