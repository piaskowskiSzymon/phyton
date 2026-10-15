def kwadratowa(a, b, c):
    delta = pow(b, 2) - (4 * a * c)
    if(delta < 0):
        print("Równanie nie ma rozwiązania")
    if(delta == 0):
        x1 = -b / (2 * a)
        print(f"rozwiązanie rówania to {x1}")
    if(delta > 0):
        x1 = (-b - delta ** (1/2)) / (2 * a)
        x2 = (-b + delta ** (1/2)) / (2 * a)
        print(f"Rozwiązania równania to {x1} oraz {x2}")

def pobierz_liczbe(komunikat):
    while True:
        try:
            return float(input(komunikat))
        except ValueError:
            print("To nie jest liczba, spróbuj jeszcze raz.")

a = pobierz_liczbe("podaj współczynnik a: ")
b = pobierz_liczbe("Podaj współczynnik b: ")
c = pobierz_liczbe("Podaj współczynnik c: ")

kwadratowa(a, b, c)