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
handler: IOHandler = AOC(13, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.split("\n\n")
    # ll = [list(map(int, line.split())) for line in data]
    # m, n = len(data), len(data[0])
    pattern = [
            r"Button A: X\+(\d+), Y\+(\d+)",
            r"Button B: X\+(\d+), Y\+(\d+)",
            r"Prize: X=(\d+), Y=(\d+)"
            ]
    pattern = "\n".join(pattern)
    pat = re.compile(pattern)

    data = [ pat.match(block).groups() for block in data ]
    data = [ [int(v) for v in block] for block in data ]
    data = [ ((ax, ay), (bx, by), (tx, ty)) for ax, ay, bx, by, tx, ty in data ]

    # =============== part a ===============
    check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

    def solve(button_a, button_b, target, costa: int = 3, costb: int = 1, offset: int = 0):
        # read in buttons as matrix
        a, c = button_a
        b, d = button_b
        px, py = target
        px += offset
        py += offset

        # equation system
        #    A    x = b
        # ( a b ) A = px
        # ( c d ) B = py
        # we invert A
        det = a * d - b * c
        a, b, c, d = d, -b, -c, a

        A = px * a + py * b
        B = px * c + py * d

        if A % det or B % det:
            return 0
        else:
            A //= det
            B //= det
            return costa * A + costb * B


    def part_a():
        return sum(solve(*block) for block in data)

    # =============== part b ===============
    def part_b():
        offset = 10000000000000
        return sum(solve(*block, offset=offset) for block in data)

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

