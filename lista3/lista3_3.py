import math

def liczby_pierwsze(n):
    def stworz_sito(s, rozmiar):
        for _ in range(rozmiar + 1):
            s.append(True)
        s[0] = False
        s[1] = False
    def wykonaj_sito(s):
        for i in range(2, len(s)):
            if s[i]:
                j = i * i
                while j < len(s):
                    s[j] = False
                    j += i
    def znajdz_n_ta(s, n):
        licznik = 0
        for i in range(len(s)):
            if s[i]:
                licznik += 1
                if licznik == n:
                    return i
    if n < 6:
        granica = 15
    else:
        granica = int(n * (math.log(n) + math.log(math.log(n)))) + 1
    s = []
    stworz_sito(s, granica)
    wykonaj_sito(s)
    return znajdz_n_ta(s, n)


def pobierz_liczbe(komunikat):
    while True:
        try:
            liczba = int(input(komunikat))
            if liczba > 0:
                return liczba
            else:
                print("Podaj liczbę dodatnią.")
        except ValueError:
            print("To nie jest liczba całkowita, podaj liczbę całkowitą")

n = pobierz_liczbe("Którą liczbę pierwszą chcesz otrzymać? ")
print(f"{n}-ta liczba pierwsza to: {liczby_pierwsze(n)}")
