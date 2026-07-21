licznik = 0

def f(a, b):
    global licznik
    if b == 0:
        return 0
    k = ostatnia(b)
    w = f(a, skroc(b))
    w = dopisz(w)
    while k > 0:
        licznik += 1
        w = w + a
        k -= 1
    return w

def skroc(a):
    return a // 10

def dopisz(a):
    return a * 10

def ostatnia(a):
    return a % 10

if __name__ == "__main__":
    #print(f(42, 2));
    #print(f(4, 125));
    #print(f(103, 104));
    #print(f(987654321, 123456789));
    #print(f(2024, 1000));
    print(f(2024, 1234))
    print(licznik)