#!/usr/bin/python3.1
# -*- coding: UTF-8 -*-

from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
import multiprocessing
import time

tyypit = ["Bob Sagget", "Cloris Leachman", "Norm MacDonald", "Greg Ricardo", "Gilbert Gottfried"]
tulokset = {}

def tee_jotain(name):
    for i in range(1,4):
        #Mikäli tässä olisi vain nukuttu sen sijaan, että tuhlataan hieman prosessoriaikaa, niin tulos
        #olisikin ollut se, että säikeet olisivat olleet nopeimpia. Ja niinhän sen täytyy olla, sillä
        #tokihan moni säije voi nukkua samaan aikaan ja lisäksi säikeet ovat (jaettu muisti) paljon
        #prosesseja kevyempiä.
        for j in range(1, 1000000):
            if j > 0:
                continue;
            break
        print(i, name)

def moniprosessitesti():
    allas = Pool(5)
    allas.map(tee_jotain, tyypit, 1)
    
def yksiprosessitesti():
    for juippi in tyypit:
        tee_jotain(juippi)
    
def säijetesti():
    säijeallas = ThreadPool(5)
    säijeallas.map(tee_jotain, tyypit, 1)

def main():
    print("Konessa on", multiprocessing.cpu_count(), "prosessoria.")
    
    for testi in [moniprosessitesti, yksiprosessitesti, säijetesti]:
        print("\n", testi.__name__)
        aloitus = time.time()
        testi()
        tulokset[testi.__name__] = time.time() - aloitus
        
    print("tulokset:")
    for avain in tulokset:
        print(avain, tulokset[avain])

if __name__ == "__main__":
    main()
