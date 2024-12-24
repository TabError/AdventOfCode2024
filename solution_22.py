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
handler: IOHandler = AOC(22, 2024, "github", live=bool(live))
# handler: IOHandler = StdIO()

# =============== snippets ===============
c = lambda s: complex(s.replace(',', '+') + 'j')
dirs = (1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j)


# =============== solution ===============
def main(data: str = handler.input()):
    # =============== preparation ===============
    data = data.splitlines()
    data = [int(v) for v in data]

    # =============== part a ===============
    check_coords = lambda c: 0 <= c.imag < m and 0 <= c.real < n

    MOD = 16777216
    assert MOD == 2 ** 24

    assert 64 == 2 ** 6
    assert 32 == 2 ** 5
    assert 2048 == 2 ** 11

    prune = lambda x: x % MOD
    mult = lambda x: prune((x << 6) ^ x)
    div = lambda x: prune((x >> 5) ^ x)
    mult2 = lambda x: prune((x << 11) ^ x)

    def next_secret(val: int) -> int:
        val = mult(val)
        val = div(val)
        val = mult2(val)
        return val

    def secrets(val: int, num: int = 2000) -> list[int]:
        ls = []
        for _ in range(num):
            val = next_secret(val)
            ls.append(val)
        return ls

    def part_a():
        return sum(secrets(v)[-1] for v in data)

    # =============== part b ===============
    def part_b():
        dd = col.defaultdict(int)

        for val in data:
            used = set()
            diffs = []
            for _ in range(2000):
                nval = next_secret(val)
                diffs.append(nval % 10 - val % 10)
                val = nval

                if len(diffs) >= 4:
                    seq = tuple(diffs[-4:])
                    if seq not in used:
                        used.add(seq)
                        dd[seq] += val % 10

        return max(dd.values())

    # =============== print ===============
    handler.submit_a(part_a())
    handler.submit_b(part_b())


if __name__ == "__main__":
    main()

