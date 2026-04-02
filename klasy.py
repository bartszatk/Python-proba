class KontoBankowe:
    def __init__(self, wlasciciel, numer_konta, saldo_poczatkowe, pin):
        self.wlasciciel = wlasciciel          # publiczne
        self._numer_konta = numer_konta       # protected
        self.__saldo = saldo_poczatkowe       # prywatne
        self.__pin = pin                      # prywatne

    def wplac(self, kwota):
        if kwota > 0:
            self.__saldo += kwota
            print(f"Wpłacono {kwota} zł")
        else:
            print("Błędna kwota")

    def wyplac(self, kwota, pin):
        if pin != self.__pin:
            print("Nieprawidłowy PIN!")
            return
        
        if kwota > self.__saldo:
            print("Brak środków")
        else:
            self.__saldo -= kwota
            print(f"Wypłacono {kwota} zł")

    def pokaz_saldo(self, pin):
        if pin == self.__pin:
            return self.__saldo
        else:
            return "Błędny PIN"

    def zmien_pin(self, stary_pin, nowy_pin):
        if stary_pin == self.__pin:
            self.__pin = nowy_pin
            print("PIN zmieniony")
        else:
            print("Błędny PIN")

    def __str__(self):
        return f"Konto właściciela: {self.wlasciciel}, nr: {self._numer_konta}"


class KontoOszczednosciowe(KontoBankowe):
    def __init__(self, wlasciciel, numer_konta, saldo_poczatkowe, pin, oprocentowanie):
        super().__init__(wlasciciel, numer_konta, saldo_poczatkowe, pin)
        self.oprocentowanie = oprocentowanie  # publiczne

    def nalicz_odsetki(self, pin):
        saldo = self.pokaz_saldo(pin)
        
        if isinstance(saldo, str):
            print(saldo)
            return
        
        odsetki = saldo * self.oprocentowanie / 100
        self.wplac(odsetki)
        print(f"Dodano odsetki: {odsetki} zł")

    def __str__(self):
        return f"Konto oszczędnościowe: {self.wlasciciel}, oprocentowanie: {self.oprocentowanie}%"

konto1 = KontoBankowe("Jan", "12345", 1000, 1111)
konto2 = KontoOszczednosciowe("Anna", "67890", 2000, 2222, 5)

konto1.wplac(500)
konto1.wyplac(200, 1111)

print(konto1.pokaz_saldo(1111))
print(konto1)

konto2.nalicz_odsetki(2222)
print(konto2.pokaz_saldo(2222))
print(konto2)
