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
handler: IOHandler = AOC(2, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)

# =============== preparation ===============
data = handler.input().splitlines()
ll = [list(map(int, line.split())) for line in data]
# m, n = len(data), len(data[0])


# =============== part a ===============
check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

def safe(l):
    d = [ b - a for a, b in zip(l[1:], l) ]
    if any(abs(e) not in [1, 2, 3] for e in d):
        return False
    return all(e > 0 for e in d) or all(e < 0 for e in d)

def part_a():
    return sum(safe(line) for line in ll)

# =============== part b ===============
def part_b():
    res = 0
    for l in ll:
        n = len(l)
        for i in range(n):
            ol = l[:i] + l[i + 1:]
            assert len(ol) == n-1
            if safe(ol):
                res += 1
                break

    return res

# =============== main ===============
def main():
    handler.submit_a(part_a())
    handler.submit_b(part_b())

    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

