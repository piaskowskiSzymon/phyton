import math

def rozklad(n):
    if n==0:
        print(0)
    if n==1:
        print(1)
    czynniki = []
    k = 2
    while n > 1:
        wykladnik = 0
        while n % k == 0:
            wykladnik += 1
            n = n // k
        if wykladnik == 1:
            czynniki.append(str(k))
        elif wykladnik > 1:
            czynniki.append(f"{k}^{wykladnik}")
        k += 1
    print(" * ".join(czynniki))

def pobierz_liczbe(komunikat):
    while True:
        try:
            return int(input(komunikat))
        except ValueError:
            print("To nie jest liczba całkowita, podaj liczbę całkowitą ")

n = pobierz_liczbe("Podaj liczbę całkowitą n, a rozłożę ją na czynniki pierwsze: ")
rozklad(n)