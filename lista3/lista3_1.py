def liczba_liczb_pierwszych(n):
    count = 0
    i = 2
    while i <= n:
        if czyPierwsza(i):
            count += 1
        i += 1
    return count

def czyPierwsza(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i <= n // i:
        if n % i == 0:
            return False
        i += 2
    return True

def pobierz_liczbe(komunikat):
    while True:
        try:
            return int(input(komunikat))
        except ValueError:
            print("To nie jest liczba całkowita, podaj liczbę całkowitą ")

n = pobierz_liczbe("Podaj liczbę całkowitą n, a sprawdzę ile jest liczb pierwszych nie większych od n: ")
print(f"Liczb pierwszych nie większych od {n} jest {liczba_liczb_pierwszych(n)}")