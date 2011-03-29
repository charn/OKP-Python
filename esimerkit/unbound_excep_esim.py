#!/usr/bin/python3.1
# -*- coding: UTF-8 -*-

muuttuja="globaali"
print("moduulitasolla", muuttuja)

def main():
    import sys
    #muuttuja on selvästi edelleen globaalien nimien joukossa
    if 'muuttuja' in globals(): print("muuttuja on määritelty globaalilla tasolla")

    try:
        #FAIL! UnboundLocalError: local variable 'muuttuja' referenced before assignmen!
        print("fail", muuttuja)
    except UnboundLocalError:
        name, msg = sys.exc_info()[:2]

    #Btw. alemmalla lohkotasolla määritellyt muuttujat näkyvät ylemmälle
    print(name.__name__+":", msg)

    #Ja syy on seuraavalla koodirivillä. Näin käy sillä kääntäjä merkitsee seuraavan
    #lauseen takia nimen muuttuja olemaan tyypiltään lokaali viittaus tässä
    #lohkossa. Siten suoritusaikana kun nimeen muuttuja viitataan yllä, sitä
    #etsitäänkin vain lokaalien muuttujien joukosta. Koska tämä lause jossa lokaali
    #nimi muuttuja sidotaan merkkijonoon "lokaali", on ensimmäisen nimeen tehdyn
    #viittauksen jälkeen tässä lohkossa, on muuttuja tässä siis vielä
    #sitomatta.
    muuttuja = "lokaali"
    print("main", muuttuja)

    def fun():
        global muuttuja
        print("funktio", muuttuja)
    fun()

    lam = lambda: print("lambda", muuttuja)
    lam()

    #Seuraava if-lause saisi kuitenkin aikaan sen, että kaikkialla main-metodissa
    #tunnus muuttuja viittaisi saman nimiseen moduulitason globaaliin muuttujaan.
    #Tämä ei toki sinänsä liene kovin yllättävää, mutta toimii kuitenkin pienenä
    #demonstraatio siitä, että if-lause ei ole lohko. Ei ainakaan Pythonissa :)
    #if True:
    #    global muuttuja
    #    print("globaali", muuttuja)

if __name__ == '__main__':
    main()
    print("moduulitasolla if-lohkossa", muuttuja)
