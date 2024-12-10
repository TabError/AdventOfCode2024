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
handler: IOHandler = AOC(4, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)

# =============== preparation ===============
data = handler.input().splitlines()
# ll = [list(map(int, line.split())) for line in data]
m, n = len(data), len(data[0])

posls = col.defaultdict(set)
for i, row in enumerate(data):
    for j, c in enumerate(row):
        posls[c].add(complex(j, i))

# =============== part a ===============
check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

def check_word(p: complex, d: complex, word: str):
    pls = [ p + k * d for k in range(len(word)) ]
    return all( p in posls[c] for p, c in zip(pls, word) )

def part_a():
    word = "XMAS"

    res = 0
    for p in posls[word[0]]:
        for d in dirs:
            res += check_word(p, d, word)
    return res

# =============== part b ===============
diadirs = (1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j)

def check_xmas(p):
    if not p in posls["A"]:
        return False
    return sum(p + d in posls["M"] and p - d in posls["S"] for d in diadirs) >= 2


def part_b():
    res = 0
    for i in range(m):
        for j in range(n):
            res += check_xmas(complex(j, i))
    return res

# =============== main ===============
def main():
    handler.submit_a(part_a())
    handler.submit_b(part_b())

    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

