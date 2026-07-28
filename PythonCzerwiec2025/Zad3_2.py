def main():
    with open("res/dane.txt") as f:
        linia = f.readline().rstrip("\n")

    split = list(linia)
    cyfry = [0] * 10

    for i in range(len(split)):
        numer = -1
        try:
            numer = int(split[i])
        except ValueError:
            pass

        for j in range(len(cyfry)):
            if numer == j:
                cyfry[j] = cyfry[j] + 1

    max_val = -1
    for i in range(len(cyfry)):
        if cyfry[i] > max_val:
            max_val = cyfry[i]

    for i in range(len(cyfry)):
        if cyfry[i] == max_val:
            print(str(i) + " " + str(cyfry[i]))


if __name__ == "__main__":
    main()