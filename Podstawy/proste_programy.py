def pole_prostokata():
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    while True:
        if a < 0 or b < 0:
            a = float(input("Długości boków muszą być liczbami dodatnimi. Podaj długość boku a: "))
            b = float(input("Podaj długość boku b: "))
        else:
            return a * b
print(f"Pole prostokąta wynosi: {pole_prostokata()}")