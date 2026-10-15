def eukldes(a, b):
    while b!=0:
        a, b = b, a%b
    return abs(a)

def pobierz_liczbe(komunikat):
    while True:
        try:
            return int(input(komunikat))
        except ValueError:
            print("To nie jest liczba całkowita, spróbuj jeszcze raz.")

a = pobierz_liczbe("Podaj pierwszą liczbę: ")
b = pobierz_liczbe("Podaj drugą liczbę: ")

print(f"NWD {a} oraz {b} to {eukldes(a, b)}")