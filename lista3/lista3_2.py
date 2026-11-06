def dwumian_newtona(n, k):
    if k < 0 or k > n or n < 0:
        return 0;
    C = [0] * (k + 1)
    C[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            C[j] += C[j -1]
    return C[k] 

    

def pobierz_liczbe(komunikat):
    while True:
        try:
            return int(input(komunikat))
        except ValueError:
            print("To nie jest liczba całkowita, podaj liczbę całkowitą")

n = pobierz_liczbe("Podaj górną liczbę dwumianu Newtona: ")
k = pobierz_liczbe("Podaj dolną liczbę dwumianu Newtona: ")
print(f"Wartość dwumianu Newtona {n} po {k} wynosi {dwumian_newtona(n, k)}")

