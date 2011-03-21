import sys

def fib(n):
    """Palauttaa ensimmäisen Fibonaccin luvun, joka on syöttölukua suurempi."""
    a, b = 0, 1
    while b <= n:
        a, b = b, a+b
    return b

if __name__ == "__main__":
    try: # Yritetään lukea kokonaisluku
        n = int(input())
    except ValueError:
        sys.exit("Antamasi syöte ei ollut kokonaisluku!")
    print(fib(n))
