#!/usr/bin/python3.1
# -*- coding: UTF-8 -*-

def fib(n):
    """Palauttaa Fibonaccin lukuja, kunnes saavutetaan luku, joka on suurempi kuin syöttöluku."""
    yield 0
    a, b = 0, 1
    while b <= n:
        a, b = b, a+b
        yield a

for f in fib(20):
    print(f)
