def eka(p):
    x = "olen ekan x"
    print("--- eka alkaa ---")
    p() # tokan paikalliset eivät näy tänne.
        # funktio p käydään suorittamassa määrittelykohdan ympäristössä
    print(x)
    print("--- eka päättyy ---")

def toka():
    print("--- toka alkaa ---")
    x = "olen tokan x"
    
    def fpar():
    	nonlocal x # muuttuja x viittaa nyt sulkeuman ulkopuoliseen viimeiseksi
    	           # sidottuun tunnukseen eli tokan muuttujaan x 
    	print(x)
    	x = "tokan x on muutettu!"
    
    eka(fpar) # "nimetyn sulkeuman" välitys funktioparametrina
    print(x) # viittaus paikalliseen tunnukseen
    print("--- toka päättyy ---")

if __name__ == "__main__": # Pääohjelma
    toka()
