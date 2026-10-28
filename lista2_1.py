def Euklides(a, b):
    while b != 0:
        a, b = b, a % b
    return a;

def pobierz_liczbe(komunikat):
    while True:
        try:
            return int(input(komunikat))
        except ValueError:
            print("Nieprawidłowa wartość. Proszę wpisać liczbę.")

a = pobierz_liczbe("Podaj pierwszą liczbę:")
b = pobierz_liczbe("Podaj drugą liczbę:")

print(f"Największy wspólny dzielnik liczb {a} oraz {b} to {Euklides(a, b)}")