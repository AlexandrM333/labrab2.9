#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


def fib(n=4):
    for i in range(1, n+1):
        n += i


def factorial(n=4):
    if n == 1:
        return 1
    return n + factorial(n - 1)


print(timeit.timeit(stmt=fib, number=10000))
print(timeit.timeit(stmt=factorial, number=10000))
