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
handler: IOHandler = AOC(11, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)

# =============== preparation ===============
data = handler.input().splitlines()
# ll = [list(map(int, line.split())) for line in data]
# m, n = len(data), len(data[0])

stones = [ int(v) for v in data[0].split() ]

# =============== part a ===============
check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

def blink(stone: int) -> tuple[int]:
    if stone == 0:
        return (1,)

    s = str(stone)
    l = len(s)
    if l % 2 == 0:
        h = l // 2
        return int(s[:h]), int(s[h:])
    
    return (stone * 2024,)

def simulate_line(ls: list, blinks: int) -> list:
    if not blinks:
        return ls
    ls = [ ss for s in ls for ss in blink(s) ]
    return simulate_line(ls, blinks - 1)

def part_a():
    res = len(simulate_line(stones, 25))
    return res

# =============== part b ===============
@ft.cache
def simulate_stone(stone: int, blinks: int):
    if not blinks:
        return 1
    return sum(simulate_stone(s, blinks - 1) for s in blink(stone))

def part_b():
    res = sum(simulate_stone(s, 75) for s in stones)
    return res

# =============== main ===============
def main():
    handler.submit_a(part_a())
    handler.submit_b(part_b())

    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

