# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
from typing import *
import bisect

# =============== handler ===============
from Handler import IOHandler, StdIO, AOC

live = 1
handler: IOHandler = AOC(7, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)

# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.splitlines()
    data = [ line.replace(":", " ").split() for line in data ]
    data = [ [int(v) for v in ls] for ls in data ]

    # =============== part a ===============
    # add = lambda a, b: a + b
    # mul = lambda a, b: a * b
    from operator import add, mul

    def check(v: int, c: int, xs: list, funcs: tuple[callable]):
        if not xs:
            return v == c
        x, *xs = xs
        # return any(check(v, f(c, x), xs, funcs) for f in funcs) # any() is ridiculously slow
        for f in funcs:
            if check(v, f(c, x), xs, funcs):
                return True
        return False

    def part_a():
        funcs = (add, mul)
        res = sum(v for v, x, *xs in data if check(v, x, xs, funcs))
        return res

    # =============== part b ===============
    # con = lambda a, b: int(str(a) + str(b))
    # con = lambda a, b: a * 10 ** len(str(b)) + b
    con = lambda a, b: a * 10 ** ceil(log10(b + 1)) + b

    def part_b():
        funcs = (add, mul, con)
        res = sum(v for v, x, *xs in data if check(v, x, xs, funcs))
        return res

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

