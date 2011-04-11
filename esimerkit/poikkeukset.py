#!/usr/bin/python3.1
# -*- coding: UTF-8 -*-

class NegativeNumberError(Exception):
    pass    #Meille riittää tässä yksinkertaisen tavallisen poikkeuksen toteutus, joten jätetään tämä määrittely tyhjäksi

def main():
    try:
        print("Anna positiivinen luku:")
        jakaja = int(input())
        if jakaja < 0:
            raise NegativeNumberError("Negatiivinen numero ei ole tässä sallittu")
        1/jakaja
    except ZeroDivisionError as e:  #Tässä käsitellään vain ZeroDivisionErrorit ja poikkeus-olio välitetään käsittelevään lohkoon as-avainsanan avulla muuttujassa e
        #Seuraavassa muutamia tapoja päästä poikkeuksen tietoihin käsiksi
        import sys, traceback
        print(e.__class__.__name__)
        print(e)
        print(e.__cause__)
        print(e.__context__)
        print(e.__traceback__)
        print(sys.exc_info())
        traceback.print_tb(e.__traceback__)
    except (ValueError, NegativeNumberError): #Käsittelijä voidaan määrittää käsittelemään useamman tyyppisiä poikkeuksia.
        print("ValueError tai NegativeNumberError")
        raise
    except ZeroDivisionError:   #Tätä käsittelijää ei suoriteta koskaan, sillä käsittelijöistä valitaan aina vain yksi ja se on ensimmäinen
        #ylhäältä alas katsottuna, joka kelpaa poikkeuksen käsittelyyn.
        print("Tänne ei päädytä koskaan")
    except: #Oletus "catch"-haara. Tänne päästään ainakin ajamalla ohjelma ja jos syötteen annon sijasta painetaan ctrl + c tai ctrl + d
        print("Jokin muu meni pieleen")
    #except Exception:   #Tämä ei menisi kääntäjästä läpi, sillä oletuskäsittelijän (pelkkä except:) jälkeen ei saa määritellä enää käsittelijöitä.
    #    print("Tänne ei ole laillista")
    finally:    #Tämän haaran koodi kaikissa tapauksissa.
        print("Tämä printataan aina")

if __name__ == "__main__":
    main()
