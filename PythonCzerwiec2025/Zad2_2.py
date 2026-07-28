def euklides(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def main():
    ilosc = 0
    with open("res/liczby1.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            liczba = int(line)
            x = liczba
            dlugosc = 0
            while x > 0:
                dlugosc += 1
                x //= 10

            potega = 1
            b = 0
            for i in range(1, dlugosc // 2 + 1):
                b = b + potega * (liczba % 10)
                liczba //= 10
                potega *= 10

            a = liczba
            wynik = euklides(a, b)
            if wynik == 1:
                ilosc += 1

    print(ilosc)


if __name__ == "__main__":
    main()