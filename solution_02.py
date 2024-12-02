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

api = AOC(2, 2024, "github")

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')

# =============== preparation ===============
data = api.input().splitlines()
# data = open(0).read().splitlines()

ll = [list(map(int, line.split())) for line in data]


# =============== part 1 ===============
def safe(l):
    d = [ b - a for a, b in zip(l[1:], l) ]
    if any(abs(e) not in [1, 2, 3] for e in d):
        return False
    return all(e > 0 for e in d) or all(e < 0 for e in d)

def f1():
    return sum(safe(line) for line in ll)

# =============== part 2 ===============
def f2():
    res = 0
    for l in ll:
        n = len(l)
        for i in range(n):
            ol = l[:i] + l[i + 1:]
            assert len(ol) == n-1
            if safe(ol):
                res += 1
                break

    return res

# =============== main ===============
def main():
    a = f1()
    print(a)
    # api.submit_a(a)

    b = f2()
    print(b)
    # api.submit_b(b)


    import datetime as dt
    print(dt.datetime.now().strftime("%T:%f")[:-3])

if __name__ == "__main__":
    main()

