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
handler: IOHandler = AOC(12, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j)

# =============== preparation ===============
data = handler.input().splitlines()
# ll = [list(map(int, line.split())) for line in data]
m, n = len(data), len(data[0])

garden = {}
for i, row in enumerate(data):
    for j, g in enumerate(row):
        p = complex(j, i)
        garden[p] = g

# =============== part a ===============
check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

def gather_region(p: complex) -> tuple[set[complex], set[tuple[complex, complex]]]:
    region = {p}
    per = set()

    q = [p]
    while q:
        p = q.pop()
        for view in dirs:
            n = p + view
            if check_coords(n) and garden[p] == garden[n]: # inner border
                if n not in region:
                    q.append(n)
                    region.add(n)
            else: # outer border / perimeter
                per.add((p, view))

    return region, per

def all_regions():
    rs = []
    all_gardens = set(garden)
    while len(all_gardens) > 0:
        p = all_gardens.pop()
        r, per = gather_region(p)
        all_gardens.difference_update(r)
        rs.append((r, per))
    return rs

regions = all_regions()

def part_a():
    res = sum(len(r) * len(per) for r, per in regions)
    return res

# =============== part b ===============
def sides(per: set[tuple[complex, complex]]) -> int:
    return sum(1 for p, v in per if (p + v * 1j, v) not in per)

def part_b():
    res = sum(len(r) * sides(per) for r, per in regions)
    return res

# =============== main ===============
def main():
    handler.submit_a(part_a())
    handler.submit_b(part_b())

    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

