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
handler: IOHandler = AOC(8, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)

# =============== preparation ===============
data = handler.input().splitlines()
m, n = len(data), len(data[0])

antennas = col.defaultdict(list)
for i, row in enumerate(data):
    for j, c in enumerate(row):
        if c != ".":
            antennas[c].append(i * 1j + j)


# =============== part a ===============
check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

def part_a():
    spots = set()
    for ls in antennas.values():
        for a, b in it.combinations(ls, r=2):
            d = b - a
            if check_coords(b + d):
                spots.add(b + d)
            if check_coords(a - d):
                spots.add(a - d)

    res = len(spots)
    return res

# =============== part b ===============
def part_b():
    spots = set()
    for ls in antennas.values():
        for a, b in it.combinations(ls, r=2):
            d = b - a
            p = b
            while check_coords(p):
                spots.add(p)
                p += d
            p = a
            while check_coords(p):
                spots.add(p)
                p -= d

    res = len(spots)
    return res

# =============== main ===============
def main():
    handler.submit_a(part_a())
    handler.submit_b(part_b())

    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

