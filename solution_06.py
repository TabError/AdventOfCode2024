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

rocks = { i * 1j + j for i, row in enumerate(data) for j, c in enumerate(row) if c == "#" }
guard = [ i * 1j + j for i, row in enumerate(data) for j, c in enumerate(row) if c == "^" ]
assert len(guard) == 1
start = (guard[0], -1j)

# =============== part a ===============
check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

type history = set[tuple[complex, complex]]

def simulate(guard: complex, move: complex, hist: history = set(), part_b: bool = False) -> str:
    hist = hist.copy()
    histpos = {p for p, _ in hist}
    obs = set()
    while True:
        if (guard, move) in hist:
            return Ellipsis
        else:
            hist.add((guard, move))
            histpos.add(guard)

        nextpos = guard + move
        if nextpos in rocks:
            move *= 1j
        else:
            if not check_coords(nextpos):
                return histpos if not part_b else obs

            if part_b and nextpos not in histpos:
                rocks.add(nextpos)
                if simulate(guard, move * 1j, hist) is Ellipsis:
                    obs.add(nextpos)
                rocks.remove(nextpos)

            guard = nextpos

def part_a():
    hp = simulate(*start)
    assert hp is not Ellipsis
    res = len(hp)
    return res

# =============== part b ===============
def part_b():
    obs = simulate(*start, part_b=True)
    assert obs is not Ellipsis
    res = len(obs)
    return res

# =============== main ===============
def main():
    handler.submit_a(part_a())
    handler.submit_b(part_b())

    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

