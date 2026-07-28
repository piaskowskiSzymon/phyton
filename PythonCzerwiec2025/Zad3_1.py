def main():
    with open("res/dane.txt", "r") as f:
        linia = f.readline().rstrip("\n")

    split = list(linia)
    ile_liczb = 0
    czy_poczatek = True

    for i in range(len(split) - 1):
        if i == 0:
            if split[i] == "5" and split[i + 1] == "0":
                ile_liczb += 1
            continue

        if 47 < ord(split[i - 1]) < 58:
            czy_poczatek = True
        else:
            czy_poczatek = False

        if split[i] == "5" and split[i + 1] == "0" and not czy_poczatek:
            ile_liczb += 1

    print(ile_liczb)


if __name__ == "__main__":
    main()