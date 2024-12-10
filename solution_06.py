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
handler: IOHandler = AOC(6, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)

# =============== preparation ===============
data = handler.input().splitlines()
# ll = [list(map(int, line.split())) for line in data]
m, n = len(data), len(data[0])

rocks = [ i * 1j + j for i, row in enumerate(data) for j, c in enumerate(row) if c == "#" ]
guard = [ i * 1j + j for i, row in enumerate(data) for j, c in enumerate(row) if c == "^" ]
assert len(guard) == 1

# =============== part a ===============
check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

def part_a():
    d = -1j
    g = guard[0]

    ps = set()
    while check_coords(g):
        ps.add(g)
        if g + d not in rocks:
            g += d
        else:
            d *= 1j
    return len(ps)

# =============== part b ===============
def part_b():
    res = 0

    return res

# =============== main ===============
def main():
    handler.submit_a(part_a())
    # handler.submit_b(part_b())

    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

