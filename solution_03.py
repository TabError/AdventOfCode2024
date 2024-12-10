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
handler: IOHandler = AOC(3, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)

# =============== preparation ===============
data = handler.input().splitlines()
# ll = [list(map(int, line.split())) for line in data]
# m, n = len(data), len(data[0])


# =============== part a ===============
check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

def part_a():
    pat = r"mul\((\d+),(\d+)\)"
    p = re.compile(pat)

    res = 0
    for l in data:
        ls = p.findall(l)
        ls = [ (int(a), int(b)) for a, b in ls ]
        res += sum(a * b for a, b in ls)

    return res


# =============== part b ===============
def part_b():
    pat = r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"
    p = re.compile(pat)

    res = 0
    enable = True
    for l in data:
        ls = p.findall(l)

        for item in ls:
            if item[3]: # do()
                enable = True
            elif item[4]: # don't()
                enable = False
            else:
                if enable:
                    res += int(item[1]) * int(item[2])

    return res

# =============== main ===============
def main():
    handler.submit_a(part_a())
    handler.submit_b(part_b())

    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

