#!/usr/bin/python3.1
# -*- coding: UTF-8 -*-

animals = [ ('Cat', 'Meow'),
            ('Cow', 'Moo'),
            ('Dog', 'Woof')]

for animal, sound in animals:
    print("{0} says {1}!".format(animal, sound))
