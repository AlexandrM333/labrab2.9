#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Напечатать в обратном порядке последовательность чисел,
# признаком конца которой является 0.#

chislo, obratnoe = int(input()), []
while chislo != 0:
    obratnoe.append(chislo)
    chislo = int(input())
print(*obratnoe[::-1])
