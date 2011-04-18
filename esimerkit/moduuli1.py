#!/usr/bin/python3.1
# -*- coding: UTF-8 -*-
# moduuli1.py

class Luokka:
    from moduuli2 import tee_jotain
    def tee_jotain_muuta(self):
        print("Moduulissa 1 määritelty")
    
def main():
    l = Luokka()
    l.tee_jotain()
    l.tee_jotain_muuta()
    
if __name__ == "__main__":
    main()
