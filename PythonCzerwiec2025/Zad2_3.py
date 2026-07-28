def main():
    max_stopien = 0
    max_liczba = -1

    with open("res/liczby2.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            liczba = int(line)
            kwadrat_liczby = int(pow(liczba, 2))

            dlugosc = 0
            x = kwadrat_liczby
            while x > 0:
                dlugosc += 1
                x //= 10

            stopien = 0
            for i in range(dlugosc):
                potega = int(pow(10, i))
                a = kwadrat_liczby // potega
                b = kwadrat_liczby % potega
                if a + b <= liczba:
                    stopien += 1

            if stopien > max_stopien:
                max_stopien = stopien
                max_liczba = liczba

    print(max_stopien)
    print(max_liczba)


if __name__ == "__main__":
    main()