import sys

def fib(n):
    """Palauttaa ensimmäisen Fibonaccin luvun, joka on syöttölukua suurempi."""
    a, b = 0, 1
    while b <= n:
        a, b = b, a+b
    return b

if __name__ == "__main__": # Pääohjelma
    s = input("Anna fibonacci syöttöluku: ") # Lue syöte käyttäjältä
    
    # input palauttaa aina stringin, mutta haluamme kokonaisluvun
    try:
        # Yritä muuttaa syöte kokonaislukutyypiksi
        n = int(s) 
    except ValueError:
    	# Tyypin muutos epäonnistui, poistu ohjelmasta virheviestillä
        sys.exit("Antamasi syöte ei ollut kokonaisluku!")
        
    print(fib(n))
