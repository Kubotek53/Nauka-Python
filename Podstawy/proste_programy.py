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

def zakupy():
    # Ilość produktów dostępnych w sklepie
    produkty = {pomidory: 6, ogorki: 4, chleb: 9, mleko: 20, jajka: 100}
    # Ceny produktów
    ceny_produktow = {cena_pomidory: 3.50, cena_ogorki: 4.20, cena_chleb: 2.50, cena_mleko: 3.00, cena_jajka: 2.00}
    koszyk = {}
    while True:
        produkt = input("Podaj nazwę produktu do dodania do koszyka (lub wpisz 'koniec' aby zakończyć): ")
        if produkt in produkty:
            ilosc = int(input(f"Ile {produkt} chcesz dodać do koszyka? "))
            if ilosc <= produkty[produkt]:
                koszyk[produkt] = koszyk.get(produkt, 0) + ilosc
                produkty[produkt] -= ilosc
                print(f"Dodano {ilosc} {produkt}(ów) do koszyka.")
            elif produkt == 'koniec':
                break
            else:
                print(f"Niestety, mamy tylko {produkty[produkt]} {produkt}(ów) w magazynie.")
        else:
            print("Produkt nie jest dostępny w sklepie.")


            
    


    
            

            
                


