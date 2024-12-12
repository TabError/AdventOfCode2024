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
handler: IOHandler = AOC(10, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.splitlines()
    data = [list(map(int, line)) for line in data]
    m, n = len(data), len(data[0])

    heights = col.defaultdict(set)
    for i, row in enumerate(data):
        for j, h in enumerate(row):
            heights[h].add(j + 1j * i)

    # =============== part a ===============
    check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

    def compute():
        scs = {}
        rts = {}
        for p in heights[9]:
            scs[p] = {p}
            rts[p] = 1

        for h in reversed(range(9)):
            for p in heights[h]:
                neighbors = [ p + d for d in dirs if check_coords(p + d) ]

                sets = [ scs[n] for n in neighbors if n in heights[h + 1] ]
                scs[p] = set().union(*sets)

                num_paths = [ rts[n] for n in neighbors if n in heights[h + 1] ]
                rts[p] = sum(num_paths)

        score = sum(len(scs[p]) for p in  heights[0])
        rating = sum(rts[p] for p in  heights[0])
        return score, rating

    score, rating = compute()

    def part_a():
        return score

    # =============== part b ===============
    def part_b():
        return rating

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

