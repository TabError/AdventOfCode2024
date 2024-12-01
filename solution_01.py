# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
from typing import *

from aocd import get_puzzle, submit

# =============== defaults ===============
c = lambda s: complex(s.replace(',', '+') + 'j')


# =============== preparation ===============

puzzle = get_puzzle(year=2024, day=1)
data = puzzle.input_data.splitlines()

ll = [map(int, s.split()) for s in data]
a, b = zip(*ll)

# =============== part 1 ===============

def f1():
    res = 0
    for c, d in zip(sorted(a), sorted(b)):
        res += abs(c - d)
    return res


# =============== part 2 ===============

def f2():
    ca = col.Counter(a)
    cb = col.Counter(b)

    res = 0
    for v, q in ca.items():
        res += q * v * cb.get(v, 0)

    return res


# =============== main ===============

def main():
    a = f1()
    print(a)
    # submit(a)

    b = f2()
    print(b)
    # submit(b)

if __name__ == "__main__":
    main()

