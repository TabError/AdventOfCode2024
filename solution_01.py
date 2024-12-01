# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
from typing import *

# =============== aocd ===============
from AOC import AOC

api = AOC(1, 2024, "github")
# api = AOC(1, 2024, "reddit")

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')

# =============== preparation ===============
data = api.input().splitlines()

ll = [map(int, line.split()) for line in data]
la, lb = zip(*ll)

# =============== part 1 ===============
def f1():
    res = 0
    for c, d in zip(sorted(la), sorted(lb)):
        res += abs(c - d)
    return res

# =============== part 2 ===============
def f2():
    ca = col.Counter(la)
    cb = col.Counter(lb)

    res = 0
    for v in ca:
        res += v * ca.get(v) * cb.get(v, 0)

    return res

# =============== main ===============
def main():
    a = f1()
    print(a)
    api.submit_a(a)

    b = f2()
    print(b)
    api.submit_b(b)

if __name__ == "__main__":
    main()

