# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
from typing import *
import bisect

import datetime as dt

# =============== handler ===============
from Handler import IOHandler, StdIO, AOC

live = 1
handler: IOHandler = AOC(7, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)

# =============== preparation ===============
data = handler.input().splitlines()
data = [ line.split(":") for line in data ]
data = [ (int(v), list(map(int, ls.split()))) for v, ls in data ]

# =============== part a ===============
add = lambda a, b: a + b
mul = lambda a, b: a * b

def check(v: int, c: int, ls: list, funcs: tuple[callable]):
    if not ls:
        return v == c
    n = ls[0]
    ls = ls[1:]
    return any(check(v, f(c, n), ls, funcs) for f in funcs) # any() is ridiculously slow

def part_a():
    funcs = (add, mul)
    res = sum(v for v, ls in data if check(v, ls[0], ls[1:], funcs))
    return res

# =============== part b ===============
# con = lambda a, b: int(str(a) + str(b))
con = lambda a, b: a * 10 ** len(str(b)) + b
# con = lambda a, b: a * 10 ** ceil(log(b + 1, 10)) + b

def part_b():
    funcs = (add, mul, con)
    res = sum(v for v, ls in data if check(v, ls[0], ls[1:], funcs))
    return res

# =============== main ===============
def main():
    handler.submit_a(part_a())
    handler.submit_b(part_b())

    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

