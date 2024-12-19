# =============== imports ===============
import re, copy
import itertools as it
import functools as ft
import collections as col
import queue
from math import *
import bisect

# =============== handler ===============
from Handler import IOHandler, StdIO, AOC

live = 1
handler: IOHandler = AOC(19, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    patterns, designs = data.split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.splitlines()

    # =============== part a ===============
    @ft.cache
    def possibilities(d: str) -> int:
        if not d:
            return 1
        return sum(possibilities(d[len(p):]) for p in patterns if d.startswith(p))

    def part_a():
        return sum(bool(possibilities(d)) for d in designs)

    # =============== part b ===============
    def part_b():
        return sum(possibilities(d) for d in designs)

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

