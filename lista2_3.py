import math

def rozklad(n):
    if n < 2:
        print("Nie można rozłożyć na czynniki pierwsze")
        return
    k = 2
    mnozenie = True
    while n > 1:
        wykladnik = 0
        while n % k == 0:
            wykladnik += 1
            n = n // k
        if wykladnik > 0:
            if mnozenie == False:
                print(" * ", end="")
            if wykladnik == 1:
                print(k, end="")
            else:
                print(f"{k}^{wykladnik}", end="")
            mnozenie = False
        k += 1
    if n > 1:
        if mnozenie == False:
            print(" * ", end="")
        print(n)
    print()
def pobierz_liczbe(komunikat):
    while True:
        try:
            return int(input(komunikat))
        except ValueError:
            print("To nie jest liczba całkowita, podaj liczbę całkowitą ")

n = pobierz_liczbe("Podaj liczbę całkowitą n, a rozłożę ją na czynniki pierwsze: ")
rozklad(n)