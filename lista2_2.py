import math

def czyPierwsza(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def pobierz_liczbe(komunikat):
    while True:
        try:
            return int(input(komunikat))
        except ValueError:
            print("To nie jest liczba całkowita, podaj liczbę całkowitą ")

n = pobierz_liczbe("Podaj liczbę całkowitą n, a sprawdzę czy jest liczbą pierwszą: ")
if(czyPierwsza(n)):
    print(f"{n} jest liczbą pierwszą")
else:
    print(f"{n} nie jest liczbą pierwszą")