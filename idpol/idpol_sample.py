#!/usr/bin/python3.7

import idpol

biblefile = open('thebible.txt')

bible = biblefile.readlines()

for line in bible:
    print(idpol.dumpling(line.lower()))