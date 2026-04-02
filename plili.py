# 1. Wczytaj dane z pliku
def wczytaj_dane(nazwa_pliku):
    dane = []
    plik = open(nazwa_pliku, "r")
    
    for linia in plik:
        czesci = linia.strip().split(" ")
        nazwa = czesci[0]
        ilosc = int(czesci[1])
        cena = int(czesci[2])
        
        dane.append([nazwa, ilosc, cena])
    
    plik.close()
    return dane


# 2. Oblicz całkowitą wartość sprzedaży
def wartosc_sprzedazy(dane):
    suma = 0
    
    for produkt in dane:
        ilosc = produkt[1]
        cena = produkt[2]
        suma = suma + (ilosc * cena)
    
    print("Całkowita wartość sprzedaży:", suma)


# 3. Najdroższy towar
def najdrozszy(dane):
    max_cena = dane[0][2]
    nazwa = dane[0][0]
    
    for produkt in dane:
        if produkt[2] > max_cena:
            max_cena = produkt[2]
            nazwa = produkt[0]
    
    print("Najdroższy towar:", nazwa)


# 4. Najtańszy towar
def najtanszy(dane):
    min_cena = dane[0][2]
    nazwa = dane[0][0]
    
    for produkt in dane:
        if produkt[2] < min_cena:
            min_cena = produkt[2]
            nazwa = produkt[0]
    
    print("Najtańszy towar:", nazwa)


# --- Program główny ---
dane = wczytaj_dane("orders.txt")

wartosc_sprzedazy(dane)
najdrozszy(dane)
najtanszy(dane)
