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
handler: IOHandler = AOC(18, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    rawdata = data.splitlines()
    data = [ c(line) for line in rawdata]
    # m, n = len(data), len(data[0])

    # =============== part a ===============
    check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

    m, n = 71, 71

    neighbors = lambda p: [p + d for d in dirs if check_coords(p + d)]

    def dfs(start, end, bts: list[complex]):
        q = queue.Queue()
        q.put((start, 0))
        used = {start}

        while not q.empty():
            p, d = q.get()
            if p == end:
                return d
            for n in neighbors(p):
                if n in bts or n in used:
                    continue
                q.put((n, d + 1))
                used.add(n)
        return None

    def part_a():
        start = 0 + 0j
        end = 70 + 70j

        res = dfs(start, end, data[:1024])
        return res

    # =============== part b ===============
    def part_b():
        start = 0 + 0j
        end = 70 + 70j
        keyf = lambda i: not bool(dfs(start, end, data[:i]))

        res = bisect.bisect_left(range(len(data)), True, key=keyf) # the first index of a true value i.e. the first number when it becomes impossible
        res -= 1
        assert dfs(start, end, data[:res])
        assert not dfs(start, end, data[:res + 1])

        res = rawdata[res]
        return res

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

