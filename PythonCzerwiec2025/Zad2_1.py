def main():
    k = 120056
    dlugosc = 0
    x = k
    while x > 0:
        x = x // 10
        dlugosc += 1

    potega = 1
    b = 0
    for i in range(1, dlugosc // 2 + 1):
        b = b + potega * (k % 10)
        k = k // 10
        potega *= 10

    a = k
    print(str(a) + " " + str(b))


if __name__ == "__main__":
    main()