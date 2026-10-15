def czyPalindrom(n, p):
    if n < 0 or p < 2:
        raise ValueError("liczba n musi być większa bądź równa 0 a podstawa większa bądź równa 2")

    odwrocona = 0
    reszta = n
    while(reszta>0):
        odwrocona = odwrocona * p + reszta % p
        reszta //= p
    return odwrocona == n

def pobierzLiczbe(komunikat):
    while True:
        try:
            return int(input(komunikat))
        except ValueError:
            print("To nie jest liczba całkowita, podaj liczbę całkowita")

n = pobierzLiczbe("Podaj liczbę n którą chcesz sprawdzić czy jest palindromem: ")
p = pobierzLiczbe("Podaj podstawę p w której chcesz sprawdzić liczbę n: ")

if(czyPalindrom(n, p)):
    print(f"{n} jest palindromem w systemie o podstawie {p}")
else:
    print(f"{n} nie jest palindromem w systemie o podstawie {p}")