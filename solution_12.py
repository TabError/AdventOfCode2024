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
handler: IOHandler = AOC(12, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j)

# =============== solution ===============

def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.splitlines()
    # ll = [list(map(int, line.split())) for line in data]

    garden = {}
    for i, row in enumerate(data):
        for j, typ in enumerate(row):
            garden[complex(j, i)] = typ

    # =============== part a ===============
    def gather_region(p: complex) -> tuple[set[complex], set[tuple[complex, complex]]]:
        region = {p}
        per = set()

        q = [p]
        while q:
            p = q.pop()
            for view in dirs:
                n = p + view
                if n in garden and garden[p] == garden[n]: # inner border
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

    def part_a():
        regions = all_regions()
        res = sum(len(r) * len(per) for r, per in regions)
        return res

    # =============== part b ===============
    def sides(per: set[tuple[complex, complex]]) -> int:
        return sum(1 for p, v in per if (p + v * 1j, v) not in per)

    def part_b():
        regions = all_regions()
        res = sum(len(r) * sides(per) for r, per in regions)
        return res

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

