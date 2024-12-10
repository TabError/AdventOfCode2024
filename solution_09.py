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
handler: IOHandler = AOC(9, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)

# =============== preparation ===============
data = handler.input().splitlines()

diskmap = [int(c) for c in data[0].strip()]
disk = []
for i, l in enumerate(diskmap):
    if i % 2 == 0:
        disk += [i // 2] * l
    else:
        disk += [-1] * l

# =============== part a ===============
check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

def compact(d: list) -> list:
    ls = d.copy()
    f = 0
    while True:
        if f >= len(ls):
            break
        if ls[f] == -1:
            ls[f] = ls.pop()
        else:
            f += 1
    return ls

def checksum(d: list) -> int:
    return sum(i * e for i, e in enumerate(d) if e >= 0)

def part_a():
    ls = compact(disk)
    res = checksum(ls)
    return res

# =============== part b ===============
def part_b():
    ps = [0]
    for e in diskmap:
        ps.append(ps[-1] + e)

    holes = col.defaultdict(list)
    files = {}
    for i, (p, q) in enumerate(zip(ps, ps[1:])):
        if i % 2: # hole
            holes[q-p].append(p)
        else: # file
            files[p] = (i // 2, q - p)

    ls = disk.copy()
    for i in range(10):
        holes[i].append(inf)
    for fp, (fid, fl) in reversed(files.items()):
        k = sorted(list(range(fl, 10)), key = lambda i: holes[i][0])[0]
        p = holes[k][0]
        if fp <= p:
            continue
        # print(f"{fid=} from {fp=} with {fl=} goes to -> {p=} with {k=}")
        ls[p : p + fl] = [fid] * fl
        ls[fp : fp + fl] = [-1] * fl
        del holes[k][0]
        # print(f"new hole of len {k - fl} at pos {p + fl}")
        bisect.insort(holes[k - fl], p + fl)

    res = checksum(ls)
    return res

# =============== main ===============
def main():
    handler.submit_a(part_a())
    handler.submit_b(part_b())

    print(dt.datetime.now().strftime("%T:%f")[:-3])
    print()


if __name__ == "__main__":
    main()

